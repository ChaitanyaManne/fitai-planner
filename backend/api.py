from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.agents.diet_agent import DietPlanAgent
import asyncio

app = FastAPI()
diet_agent = DietPlanAgent()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-plan")
async def generate_plan(data: dict):
    age = data.get("age")
    weight = data.get("weight")
    preferences = data.get("preferences")
    goal = data.get("goal")

    result = await diet_agent.run(age, weight, goal, preferences)
    return {"plan": result}
