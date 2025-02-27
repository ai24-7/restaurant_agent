import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
WIKI_USER_AGENT = os.getenv("WIKI_USER_AGENT")

HF_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMBED_DIM = 384
# INDEX_NAME = "menuai-large"  # Name for the Pinecone index
PINECONE_INDEX_NAME = "menuai-large"
SEARCH_URL = "https://api.langsearch.com/v1/web-search"

os.environ["LANGSMITH_TRACING"] = "true"
LANGSMITH_PROJECT="pr-respectful-control-33"
os.environ["LANGSMITH_PROJECT"] = LANGSMITH_PROJECT
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
os.environ["LANGSMITH_ENDPOINT"] = LANGSMITH_ENDPOINT
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")