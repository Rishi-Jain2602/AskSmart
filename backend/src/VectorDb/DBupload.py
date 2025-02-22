from .Data_Split import process_documents
import weaviate.classes as wvc
from .schema import create_collection
import os

def weaviate_ret(path,docuemtID,filename):
    chunked_text = process_documents(path)
    chunks_list = []
    doct_name = os.path.basename(path)
    collection_creation = create_collection(filename)
    chunks = collection_creation[0]
    collection_name = collection_creation[1]

    for i, chunk in enumerate(chunked_text):
        print(f"chunk {i} type: {type(chunk)}")
        # If it's bytes, decode it
        if isinstance(chunk, bytes):
            chunk = chunk.decode("utf-8")
        data_properties = {
            "Document_title": str(doct_name),
            "chunk": str(chunk),
            "chunk_index": i,
            "DoctID": str(docuemtID)
        }
        data_object = wvc.data.DataObject(properties=data_properties)
        chunks_list.append(data_object)

    
    batch_size = 100  
    for i in range(0, len(chunks_list), batch_size):
        batch = chunks_list[i:i + batch_size]
        chunks.data.insert_many(batch)

    return collection_name