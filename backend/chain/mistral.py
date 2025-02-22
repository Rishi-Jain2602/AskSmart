from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from .prompt import Query_Prompt
from dotenv import load_dotenv
import os
load_dotenv()
# Mistral_API = os.environ("MISTRAL_API_KEY")
llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
    # api_key=Mistral_API
)
embeddings = MistralAIEmbeddings(model="mistral-embed")
parser = StrOutputParser()

chain = Query_Prompt | llm | parser
