from fastapi import FastAPI
from pydantic import BaseModel
from agents.agent import MultiToolAgent

app = FastAPI()
agent = MultiToolAgent()

class Query(BaseModel):
    prompt: str

@app.post("/chat/")
async def chat(query: Query):
    response = agent.run(query.prompt)
    return {"response": response}
