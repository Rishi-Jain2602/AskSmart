from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, JSONLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter

def process_documents(file_path):
    documents = ""
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
    elif file_path.endswith(".json"):
        loader = JSONLoader(file_path,jq_schema=".",text_content=False,json_lines=False)
    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    else:
        print(f"Unsupported file format: {file_path}")

    try:
        documents = loader.load()
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
    
    text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    return docs
