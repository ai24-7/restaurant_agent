from utils.config import SEARCH_API_KEY, SEARCH_URL
import requests

# LangSearch API tool
def langsearch_api_tool(query: str) -> str:
    """
    Queries LangSearch for external data on languages or phrases.
    """
    url = SEARCH_URL
    headers = {'Authorization': SEARCH_API_KEY}
    payload = {
        "query": query,
        "freshness": "oneYear",
        "summary": True
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    summary = []
    url_list = []
    for result in data['data']['webPages']['value'][:3]:  # Top 3 results
        summary.append(result['summary'])
        url_list.append(result['url'])
    return f"""
    LangSearch results for {query} are: \n
    {summary[0]}. Reference: {url_list[0]} \n
    {summary[1]}. Reference: {url_list[1]} \n
    {summary[2]}. Reference: {url_list[2]} \n
    """