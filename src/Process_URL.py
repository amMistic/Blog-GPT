from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.embedding import embedding_function
from dotenv import load_dotenv
import datetime
import os

# export all environment variables
load_dotenv()

# isolate each blog vector storage from each other  
unique_id = datetime.datetime.now().strftime("%d:%m:%Y:%H:%M:%S").replace(":", '')
CHORMA_PATH = f'BLOG_DATABASE\chroma_{unique_id}'
os.makedirs(CHORMA_PATH)

class Process:
    def __init__(self,) -> None:
        self.url = None
        self.document = None
        self.vector_store = None
    
    def extract_content(self, url:str):
        loader = WebBaseLoader(url)
        document = loader.load()
        self.document = document
        return document
    
    def get_vector_store(self, url:str):
        self.url = url
        content = self.extract_content(url)
        
        # Initialize the Text Splitter correctly
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(content)
        
        vector_store = Chroma.from_documents(
            chunks, embedding_function(), persist_directory=CHORMA_PATH
        )
        self.vector_store = vector_store
        return vector_store
    