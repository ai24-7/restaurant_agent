from utils.config import OPENAI_API_KEY
import pandas as pd
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

#df = pd.read_csv("data/sample2.csv")
#engine = create_engine("sqlite:///sample.db")
engine = create_engine('sqlite:///data/sample.db')

#df.to_sql("sample", engine, index=False, if_exists="append", )
db = SQLDatabase(engine=engine)
# print(db.dialect)
# print(db.get_usable_table_names())

from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
prefix = """You are an expert SQL Agent. 
The database you are connected to has a table named 'sample' with these columns:
- 'restaurant_name' (text)
- 'menu_category' (text)
- 'menu_item' (text)
- 'menu_description' (text)
- 'price_numeric' (integer)
- 'rating' (integer)
- 'review_count' (integer)
- 'address1' (text)
- 'city' (text)
- 'zip_code' (integer)
- 'country' (text)
- 'state' (text)
- 'categories' (text)
- 'ingredient_name' (text)
- 'confidence' (integer)
- 'item_id' (integer)
Use this schema to answer questions accurately."""
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)
agent_executor = create_sql_agent(llm, db=db, verbose=True, prefix=prefix )

# agent_executor.invoke({"input": "compare the average price of mexican restaurants and italian restaurants in san fracnciso"})

def query_sql_agent_tool(query: str):
    """
    Run a query (string) against the agent_executor
    and return the chain’s response.
    """
    response = agent_executor.invoke({"input": query})
    return response


# from langchain.prompts.chat import (
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
#     ChatPromptTemplate,
# )
# from langchain.schema import AIMessage

# system_template = """You are an expert SQL Agent. 
# The database you are connected to has a table named 'sample' with these columns:
# - city (text)
# - price (integer)
# - restaurant_name (text)
# - ...
# Use this schema to answer questions accurately.
# """

# system_message = SystemMessagePromptTemplate.from_template(system_template)
# human_message = HumanMessagePromptTemplate.from_template("{input}")

# chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])

# # Then create your chain/agent with that prompt:
# agent_executor = create_sql_agent(
#     llm=ChatOpenAI(
#         model="gpt-3.5-turbo", 
#         temperature=0, 
#         openai_api_key=OPENAI_API_KEY
#     ),
#     db=db,
#     prompt=chat_prompt,
#     agent_type="openai-tools",
#     verbose=True
# )
