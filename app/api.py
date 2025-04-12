from fastapi import FastAPI, Request
from agents.stateful_agent import StatefulAgent

app = FastAPI()
agent = StatefulAgent()

@app.post("/chat")
async def chat(req: Request):
    body = await req.json()
    message = body.get("message", "")
    result = agent.chat(message)
    return {"response": result.response}
