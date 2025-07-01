from langchain_community.vectorstores import Chroma
from langchain_openai import OpneAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('OPENAI_API_KEY')
embeddingmodel = OpneAIEmbeddings(model = "text-embedding-3-small")

def create_vdb(docs, dir_path):
    vecstore = Chroma.from_documents(
        collection_name = 'jd_store',
        documents = docs,
        persist_directory = dir_path
    )
    return vecstore