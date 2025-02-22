# AskSmart: A RAG-Powered Intelligent Query System


**AskSmart** is a powerful document retrieval system that allows you to upload and process various formats such as **PDF, DOCX, JSON, and TXT**. Our advanced AI technology retrieves relevant information and generates context-aware responses to your queries.

**Supported Formats: PDF, DOCX, JSON, TXT**
****
## Local Environment Setup

1. Clone the Repository
   
``` bash
git clone https://github.com/Rishi-Jain2602/AskSmart.git
```

2. Create Virtual Environment

```bash
cd backend
virtualenv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. Install the Project dependencies

- 3.1 Navigate to the **Backend** Directory and install Python dependencies:

```bash
cd backend
pip install -r requirements.txt
```
- 3.2 Navigate to the **Frontend** Directory and install Node.js dependencies:
```bash
cd frontend
npm install
```

4. Run the React App

Start the React app with the following command:

```bash
cd frontend
npm start
```

5. Run the Backend (FastAPI App)

Open a new terminal and run the backend:

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
- The server will be running at `http://127.0.0.1:8000`.



****
## Ingestion Pipeline

This code is responsible for processing and storing documents that are uploaded by users, preparing them for retrieval and generation of context-based responses. Here's how the pipeline works:

1. **File Upload**: 
   The user uploads a document (PDF, DOCX, JSON, or TXT) through an API endpoint (`/Rag/upload`), which is saved locally in a designated folder.
   ```python
   doc_id = str(uuid.uuid4())
   file_location = os.path.join(UPLOAD_DIR, f"{doc_id}_{file.filename}")
   with open(file_location, "wb") as buffer:
       shutil.copyfileobj(file.file, buffer)
   ```

2. **Document Processing**:
   After uploading, the file is processed using specific loaders based on its file type (e.g., `PyPDFLoader` for PDFs, `Docx2txtLoader` for DOCX). The document content is split into smaller text chunks to enable more efficient querying later.
   ```python
   text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
   docs = text_splitter.split_documents(documents)
   ```

3. **Data Storage**:
   These chunks are then added to a collection in Weaviate, with relevant metadata such as the document title, chunk index, and document ID.
   ```python
   data_properties = {
       "Document_title": str(doct_name),
       "chunk": str(chunk),
       "chunk_index": i,
       "DoctID": str(docuemtID)
   }
   data_object = wvc.data.DataObject(properties=data_properties)
   chunks_list.append(data_object)
   ```

4. **Chunk Insertion**:
   The chunks are inserted into Weaviate in batches to optimize performance.
   ```python
   for i in range(0, len(chunks_list), batch_size):
       batch = chunks_list[i:i + batch_size]
       chunks.data.insert_many(batch)
   ```

****

### API Endpoint Implementation

1. **Document Upload API**:
   - **Endpoint**: `POST https://asksmart.onrender.com/Rag/upload`
   - **Description**: This API allows you to upload documents in formats like PDF, DOCX, JSON, and TXT. The document is processed and stored in a Weaviate collection.
   
   **Curl Command**:
   ```bash
   curl -X POST "https://asksmart.onrender.com/Rag/upload" -F "file=@/path/to/your/file.pdf"
   ```
   - Replace `/path/to/your/file.pdf` with the actual path of the document.
   - **Response**:
   ```json
   {
     "doct_id": "Generated_collection_name",
     "filename": "yourfile.pdf",
     "message": "Upload and processing complete"
   }
   ```

2. **Chatting API**:
   - **Endpoint**: `POST https://asksmart.onrender.com/Rag/chat`
   - **Description**: Query the uploaded document to get context-based responses.
   
   **Curl Command**:
   ```bash
   curl -X POST "https://asksmart.onrender.com/Rag/chat" \
     -H "Content-Type: application/json" \
     -d '{ 
           "user_id": "SESSION_ID_VALUE", 
           "query": "CURRENT_INPUT_VALUE", 
           "doctID": "STORED_DOC_ID_VALUE" 
         }'
   ```
   - Replace `SESSION_ID_VALUE`, `CURRENT_INPUT_VALUE`, and `STORED_DOC_ID_VALUE` with actual values.
   - **Response**:
   ```json
   {
     "response": "Generated response based on document"
   }
   ```

---

### Deployment Scripts

To deploy the application, you can use the following steps:

1. **Install Dependencies**:
   - Make sure all required packages are installed. Run:
     ```bash
     pip install -r requirements.txt
     ```

2. **Environment Setup**:
   - Ensure the necessary environment variables are configured (like API keys for Weaviate, OpenAI, etc.).

3. **Run the Application**:
   - To run the FastAPI server locally:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     ```   

4. **Deploying to Render**:
   - The project is deployed to [Render](https://asksmart.onrender.com).
   - You can automate deployment with a `render.yaml` file to define the environment settings for Render, or follow manual deployment steps:
     - Create a new web service on Render.
     - Set up the build command to install dependencies and run the FastAPI server.
     - Set environment variables required for Weaviate and OpenAI integration.
     - Deploy and obtain the live URL of your application.


****

## Note
1. Make sure you have Python 3.x installed
2. It is recommended to use a virtual environment to avoid conflict with other projects.
3. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com
