# from langchain.agents import initialize_agent, AgentType
# #from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
# from langchain.tools import Tool
# from tools.vector_search import vector_search_tool
# from tools.wikipedia_api import wikipedia_api_tool
# from tools.lang_search_api import langsearch_api_tool
# from tools.pandas_tool import query_pandas_agent_tool
# from utils.config import OPENAI_API_KEY

# class MultiToolAgent:
#     def __init__(self):
#         self.llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0.01)
#         self.agent_kwargs = {
#             "verbose": True,
#             "handle_parsing_errors": True,
#             "max_iterations": 8,
#             "early_stopping_method": "generate",

#             "prefix": """Hello! I am your food and restaurant assistant. 
#             I specialize in answering questions about restaurants, menus, pricing, ingredients, and food trends. 
#             I use several tools to find the best information:

#             1. **VectorSearch** → Local restaurant data.
#             2. **WikipediaAPI** → Food trends & nutrition.
#             3. **LangSearchAPI** → External food data not available in other sources.
#             4. **PandasDataFrameTool** → When working with statistics like number of resturants or avg price comparison.

#             I will always try my best to find an answer. However, if I can’t find enough information, I will let you know instead of guessing.
#             You are using the ReAct framework, which means you must **always** follow this exact step-by-step structure in your output:

#             - Thought: (Explain your private reasoning here, not shown to the user)
#             - Action: <NameOfTool> (e.g., VectorSearch)
#             - Action Input: "<your input or query to that tool>"
#             - Observation: (the response the tool gives you)
#             - Thought: (Reflect on the new info or decide next steps)
#             - Final Answer: <the final user answer, shown to the user>
#             **If you do not follow this format exactly, the system will fail with an OutputParser error.**

#             Let's get started!""",

#                 "chain_of_thought": """Think step by step before executing any tool.

#             1) Analyze the user’s question.
#             2) Decide whether you need any tools to answer.
#             3) Use only one tool at a time with the format:
#             Action: ToolName
#             Action Input: "..."
#             4) After you get the Observation, if more info is needed, continue with another Thought → Action → Observation cycle.
#             5) Once you can answer, end with:
#             Final Answer: <your final answer here>

#             - If you need to use multiple tools, follow the same Thought → Action → Observation cycle for each tool.
#             - Make sure the output is structured, clear, and conversational.
#             - Summarize insights from multiple tools if applicable.
#             - If no data is found or the question can’t be answered, end with:
#             Final Answer: I do not have enough info to answer.

#             - Avoid extra text after Final Answer.
#             - Avoid calling the same tool repeatedly if it yields no new info.
#             """,

#                 "format_instructions": """Your final message to the user must start with:
#             Final Answer:
#             and nothing else after that line. Avoid any tool call format in the final output. Summarize or combine relevant tool observations in a friendly manner. Rely more on data comming from VectorSearch and PandasDataFrameTool."""
#         }
#         self.tools = [
#             Tool(
#                 name="VectorSearch",
#                 func=vector_search_tool.search,
#                 description="Retrieves information from vector database."
#             ),
#             Tool(
#                 name="WikipediaAPI",
#                 func=wikipedia_api_tool,
#                 description="Use this tool to get Wikipedia summaries for general information about a food or ingredients."
#             ),
#             Tool(
#                 name="LangSearchAPI",
#                 func=langsearch_api_tool,
#                 description="Performs general search for information not found in other tools."
#             ),
#             Tool(
#                 name="PandasDataFrameTool",
#                 func=query_pandas_agent_tool,
#                 description=(
#                     "Use this tool to answer questions about the restaurant dataframe, such as "
#                     "computing average prices for certain categories or filtering rows. Provide "
#                     "your query in plain English, and the agent will figure out the correct DataFrame operations."
#                     )
#             ),
#         ]

#         self.agent = initialize_agent(
#             tools=self.tools,
#             llm=self.llm,
#             agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#             verbose=True,
#             handle_parsing_errors=True,
#             max_iterations=8,
#             early_stopping_method="generate",
#             agent_kwargs= self.agent_kwargs
#         )

#     def run(self, query):
#         return self.agent.run(query)


from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool

# Tools
#from tools.clarifier_tool import clarify_user_tool
from tools.vector_search import vector_search_tool
from tools.wikipedia_api import wikipedia_api_tool
from tools.lang_search_api import langsearch_api_tool
from tools.pandas_tool import query_pandas_agent_tool

from utils.config import OPENAI_API_KEY

class MultiToolAgent:
    def __init__(self):
        # Use GPT-3.5 or GPT-4, or your custom model
        self.llm = ChatOpenAI(
            api_key=OPENAI_API_KEY,
            model="gpt-3.5-turbo",
            temperature=0.01
        )

        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.agent_kwargs = {
            "verbose": True,
            "handle_parsing_errors": True,
            "early_stopping_method": "generate",

            "prefix": """Hello! I am your food and restaurant assistant. 
            I specialize in answering questions about restaurants, menus, pricing, ingredients, and food trends. 
            I use several tools to find the best information:

            1. **VectorSearch** → Local restaurant data in san francisco
            2. **WikipediaAPI** → Food history & nutrition.
            3. **LangSearchAPI** → External food data not available in other sources such as food trends.
            4. **PandasDataFrameTool** → When working with statistics like number of resturants or avg price comparison.

            I will always try my best to find an answer. However, if I can’t find enough information, I will let you know instead of guessing.
            You are using the ReAct framework, which means you must **always** follow this exact step-by-step structure in your output:

            - Thought: (Explain your private reasoning here, not shown to the user)
            - Action: <NameOfTool> (e.g., VectorSearch)
            - Action Input: "<your input or query to that tool>"
            - Observation: (the response the tool gives you)
            - Thought: (Reflect on the new info or decide next steps)
            - Final Answer: <the final user answer, shown to the user>
            **If you do not follow this format exactly, the system will fail with an OutputParser error.**

            Let's get started!""",

                "chain_of_thought": """Think step by step before executing any tool.

            1) Analyze the user’s question.
            2) Decide whether you need any tools to answer.
            3) Use only one tool at a time with the format:
            Action: ToolName
            Action Input: "..."
            4) After you get the Observation, if more info is needed, continue with another Thought → Action → Observation cycle.
            5) Once you can answer, end with:
            Final Answer: <your final answer here>

            - If you need to use multiple tools, follow the same Thought → Action → Observation cycle for each tool.
            - Make sure the output is structured, clear, and conversational.
            - Summarize insights from multiple tools if applicable.
            - If no data is found or the question can’t be answered, end with:
            Final Answer: I do not have enough info to answer.

            - Avoid calling the same tool repeatedly if it yields no new info.
            """,

                "format_instructions": """Your final message to the user must start with:
            Final Answer:
            and nothing else after that line. Summarize or combine relevant tool observations in a friendly and coversational manner. Rely more on data comming from VectorSearch and PandasDataFrameTool."""
        }
        # Register tools
        self.tools = [
            # Tool(
            #     name="ClarifyUser",
            #     func=clarify_user_tool.run,
            #     description="Ask the user clarifying questions if there's missing info."
            # ),
            Tool(
                name="VectorSearch",
                func=vector_search_tool.search,
                description="Local restaurant data in san francisco"
            ),
            Tool(
                name="WikipediaAPI",
                func=wikipedia_api_tool,
                description="Food history & nutrition (fallback)."
            ),
            Tool(
                name="LangSearchAPI",
                func=langsearch_api_tool,
                description="External data if local info is insufficient. such as food trends."
            ),
            Tool(
                name="PandasDataFrameTool",
                func=query_pandas_agent_tool,
                description="Numeric analysis of local dataframe."
            ),
        ]

        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            #agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            #agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            memory=self.memory,
            **self.agent_kwargs
        )

    def run(self, query: str) -> str:
        """Send the user query through the ReAct agent."""
        return self.agent.run(query)
