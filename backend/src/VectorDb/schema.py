import weaviate.classes as wvc
from .config import client
import re

def sanitize_class_name(name: str) -> str:
    # Replace any non-alphanumeric character (except underscore) with an underscore
    sanitized = re.sub(r'[^A-Za-z0-9_]', '_', name)
    # Ensure the class name starts with an uppercase letter
    if sanitized and sanitized[0].islower():
        sanitized = sanitized[0].upper() + sanitized[1:]
    return sanitized

def create_collection(collection_name):

    valid_name = sanitize_class_name(collection_name)
    if client.collections.exists(valid_name): 
        client.collections.delete(valid_name) 

    chunks = client.collections.create(
        name=valid_name,
        properties=[
            wvc.config.Property(
                name="chunk",
                data_type=wvc.config.DataType.TEXT
            ),
            wvc.config.Property(
                name="Document_title",
                data_type=wvc.config.DataType.TEXT
            ),
            wvc.config.Property(
                name="chunk_index",
                data_type=wvc.config.DataType.INT
            ),
            wvc.config.Property(
                name="DoctID",
                data_type=wvc.config.DataType.TEXT
            ),
        ],
        vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),  # Use `text2vec-openai` as the vectorizer
        generative_config=wvc.config.Configure.Generative.openai(),  # Use `generative-openai` with default parameters
    )
    return [chunks,valid_name]