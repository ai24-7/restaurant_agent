
from utils.config import PINECONE_API_KEY, PINECONE_INDEX_NAME, HF_EMBEDDING_MODEL
import json
from langchain.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone

class VectorSearch:
    def __init__(
        self,
        HF_EMBEDDING_MODEL: str,
        PINECONE_API_KEY: str,
        PINECONE_INDEX_NAME: str
    ):
        """
        Initializes the VectorSearch class.

        :param HF_EMBEDDING_MODEL:      Name of the Hugging Face model to use for embeddings.
        :param PINECONE_API_KEY:     API key for accessing Pinecone.
        :param PINECONE_INDEX_NAME:  Name of the Pinecone index to query.
        """
        self.embeddings = HuggingFaceEmbeddings(model_name=HF_EMBEDDING_MODEL)

        # Initialize Pinecone
        self.pc = Pinecone(api_key=PINECONE_API_KEY)
        self.index = self.pc.Index(PINECONE_INDEX_NAME)

    def search(self, query: str, top_k: int = 3) -> str:
        """
        Perform a vector search on the Pinecone index using a string query.

        :param query: A user query string.
        :param top_k: Number of top matches to return (default: 3).
        :return:      A JSON string containing match details or a 'No matches found.' message.
        """
        # Create an embedding vector for the query
        query_vector = self.embeddings.embed_query(query)

        # Query the index
        results = self.index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )

        # Handle case if no matches are found
        if not results.matches:
            return "No matches found."

        # Gather match information into a list
        matches_list = []
        for match in results.matches:
            match_dict = {
                "id": match.id,
                "score": match.score,
                "metadata": match.metadata,
                "values": match.values  # If 'values' is included in your Pinecone metadata
            }
            matches_list.append(match_dict)

        # Wrap everything in a dictionary
        results_dict = {
            "matches": matches_list
        }

        # Return as a JSON string
        return json.dumps(results_dict)#, indent=2)

vector_search_tool = VectorSearch(HF_EMBEDDING_MODEL=HF_EMBEDDING_MODEL, PINECONE_API_KEY=PINECONE_API_KEY, PINECONE_INDEX_NAME=PINECONE_INDEX_NAME)
