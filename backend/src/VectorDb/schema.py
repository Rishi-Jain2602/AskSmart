import weaviate.classes as wvc
from .config import client

collection_name = "Rag"

if client.collections.exists(collection_name):  # In case we've created this collection before
    client.collections.delete(collection_name)  # THIS WILL DELETE ALL DATA IN THE COLLECTION

chunks = client.collections.create(
    name=collection_name,
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