import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

class WorkoutPlanAgent:

    def __init__(self):
        self.model = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model=os.getenv("MODEL")
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", 
             "You are a certified fitness trainer. Create structured daily workout plans "
             "based on user fitness level, goals, and available equipment."),
            ("human", "{query}")
        ])

    async def generate(self, user_data: dict):

        age = user_data.get("age", "Not provided")
        weight = user_data.get("weight", "Not provided")
        preferences = user_data.get("preferences", "None")
        goal = user_data.get("goal")
        experience = user_data.get("experience")
        days = user_data.get("days")

        query = f"""
            Create a {days}-day workout plan.

            User Details:
            - Goal: {goal}
            - Experience: {experience}
            - Age: {age}
            - Weight: {weight}
            - Preferences: {preferences}

            Return a clean structured plan.
        """

        chain = self.prompt | self.model
        result = chain.invoke({"query": query})
        return result.content
