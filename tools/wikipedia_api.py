# Wikipedia API tool
import wikipediaapi
from utils.config import WIKI_USER_AGENT
def wikipedia_api_tool(query: str) -> str:
    """
    Returns a summary from Wikipedia for a given query.
    """
    wiki = wikipediaapi.Wikipedia(language='en', user_agent=WIKI_USER_AGENT)
    page = wiki.page(query)
    if not page.exists():
        return f"No Wikipedia page found for {query}."
    return f"Wikipedia info about {query}: {page.summary[:500]}"