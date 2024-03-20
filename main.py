import os

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pinecone 
from langchain.vectorstores import Pinecone
from langchain.embeddings import SentenceTransformerEmbeddings
from utils import *

load_dotenv()

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

directory = '/content/data'

# initialize pinecone
pinecone.init(
    api_key=os.environ.get("OPENAI_API_KEY"),  # find at app.pinecone.io
    environment="us-east-1-aws"  # next to api key in console
)

index_name = "langchain-chatbot"

index = Pinecone.from_documents(docs, embeddings, index_name=index_name)

documents = load_docs(directory)
len(documents)

docs = split_docs(documents)
print(len(docs))

query_result = embeddings.embed_query("Hello world")
len(query_result)

query = "How is India economy"
similar_docs = get_similar_docs(query)
similar_docs

