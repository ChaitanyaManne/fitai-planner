import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

class DietPlanAgent:

    def __init__(self):
        self.model = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("MODEL")
        )

        self.prompt = ChatPromptTemplate.from_template("""
        You are a world-class dietitian.
        Create a 7-day diet meal plan based on:
        - age: {age}
        - weight: {weight}
        - goal: {goal}
        - preferences: {preferences}

        Return the plan in a clean JSON format.
        """)

    async def run(self, age, weight, goal, preferences):
        messages = self.prompt.format_messages(
            age=age, weight=weight,
            goal=goal, preferences=preferences
        )
        response = await self.model.ainvoke(messages)
        return response.content
