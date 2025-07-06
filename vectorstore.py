from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('OPENAI_API_KEY')
embeddingmodel = OpenAIEmbeddings(model = "text-embedding-3-small")

def create_vdb(docs, dir_path):
    vecstore = Chroma.from_documents(
        collection_name = 'jd_store',
        documents = docs,
        embedding = embeddingmodel,
        persist_directory = dir_path
    )
    return vecstore

def load_vectorstore(dir_path):
    persist_db = Chroma(
        persist_directory = dir_path,
        embedding_function = embeddingmodel,
        collection_name = 'jd_store'
    )
    return persist_db