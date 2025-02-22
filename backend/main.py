from fastapi import FastAPI, UploadFile, File,BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import os, shutil, uuid, uvicorn
from src.VectorDb.DBupload import weaviate_ret
from src.VectorDb.config import client
from chain.models import UserQuery
from src.VectorDb.schema import chunks
from chain.mistral import chain
from src.MongoDb.Db import conv_collection,update_db
from dotenv import load_dotenv
import logging
load_dotenv()
app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

UPLOAD_DIR = "temp_files"

@app.post("/Rag/upload")
async def upload_doc(file: UploadFile = File(...)):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    doc_id = str(uuid.uuid4())
    
    file_location = os.path.join(UPLOAD_DIR, f"{doc_id}_{file.filename}")
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    weaviate_ret(file_location, doc_id)
        
    return {
        "doc_id": doc_id,
        "filename": file.filename,
        "message": "Upload and processing complete"
    }

@app.post("/Rag/chat")
async def query(qry: UserQuery, background_tasks: BackgroundTasks):

    user_conversation = conv_collection.find_one({"user_id": qry.user_id})
    if user_conversation:
        history_messages = user_conversation["conversations"]
    else:
        history_messages = []

    response = chunks.generate.fetch_objects(
        limit=5,
        grouped_task=qry.query,
    )
    print(response.generated)
    
    if response.generated is None:
        return {"response":"Please upload a document"}

    data = ""
    Objects = response.objects
    for obj in Objects:
        data += obj.properties["chunk"]
    
    response = chain.invoke({
        "query":qry.query,
        "context":data,
        "history":history_messages
    })
    background_tasks.add_task(update_db,qry.user_id,qry.query,response)
    return {"response":response}

@app.on_event("shutdown")
async def shutdown_event():
    client.close()

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)