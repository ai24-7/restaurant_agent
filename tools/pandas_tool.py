from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from utils.config import OPENAI_API_KEY

df = pd.read_csv("data/sample.csv")
llm_for_df = ChatOpenAI(temperature=0.1, model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)
pandas_agent = create_pandas_dataframe_agent(llm_for_df, df, verbose=True, allow_dangerous_code=True,)
# pandas_agent.run("compare number of sushi and pizza in menus")

def query_pandas_agent_tool(query: str) -> str:
    """Calls the stand-alone Pandas agent on the provided query string."""
    return pandas_agent.run(query)