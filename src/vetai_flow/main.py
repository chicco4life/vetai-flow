#!/usr/bin/env python
from random import randint
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from vetai_flow.crews.poem_crew.poem_crew import Vetai2
from crewai import Agent, Crew, Process, Task

#Setup
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import pandas as pd
import sys
from typing import Literal
import yaml
from pathlib import Path


class UserInput(BaseModel):
    user: str = ""
    pet_name: str = ""
    pet_type: str = ""
    pet_age: int = None
    pet_lifestage: Literal["puppy", "adult", "senior", "breeding"] = ""
    pet_weight: float = None
    exercise_level: Literal["minimal", "low", "moderate", "high"] = ""
    message: str = "" #"I have a toy poodle, she is 7 years old, and 3.3kg. She has mild mitral valve regurgitation.  She is otherwise healthy. What supplement should she take and how much?"
    

class VetFlow(Flow[UserInput]):

    @start()
    def get_user_input(self):
        print("Getting user input")

        # Collect user input
        user = input("What is your name? ")
        pet_name = input("What is your pet's name? ")
        pet_type = input("What breed is your pet? ")
        pet_age = input("How old is your pet? ")
        pet_lifestage = input("What is your pet's life stage? ")
        pet_weight = input("How much does your pet weigh (in kg)? ")
        exercise_level = input("How much does your pet exercise? ")
        message = input("Anything else you want to tell me about your pet? ")

        # Create UserInput object with both fields
        user_input = UserInput(
            user=user,
            pet_name=pet_name,
            pet_type=pet_type,
            pet_age=pet_age,
            pet_lifestage=pet_lifestage if pet_lifestage else None,
            pet_weight=pet_weight,
            exercise_level=exercise_level if exercise_level else None,
            message=message
        )

        return user_input

    """
    @listen(get_user_input)
    def analyze_user_input(self):
        print("Analyzing user input")

        #load tasks and agents
        agents_config = 'crews/poem_crew/config/agents.yaml'
        tasks_config = 'crews/poem_crew/config/tasks.yaml'

        task = Task(
            description=
                "Parse the user message and extract information about their pet. "
                "Store all extracted information in a structured format matching these fields: "
                "- user: The name of the person (if provided) "
                "- pet_type: Type of pet (dog, cat, etc.) "
                "- pet_age: Age of the pet in years (as a number) "
                "- pet_breed: Breed of the pet (e.g., Toy Poodle, Siamese) "
                "- pet_lifestage: One of [puppy, adult, senior, breeding] "
                "- pet_weight: Weight of the pet in kg (as a number) "
                "- exercise_level: One of [minimal, low, moderate, high] "
                "- message: Any additional health concerns or questions "
                "\n\n"
                "Return the information as a JSON object with these exact field names. "
                "If information is missing, ask the user to provide this information until all fields are filled."
            ,
            agent=self.agents_config['assistant']
        )
        # Implement logic to execute this task, including asking for additional info if needed
        result = self.execute_task(task)
        self.state.pet_data = result
        return result
    """

    @listen(get_user_input)
    def calculate_nutrition(self, user_input: UserInput):
        print("calculating nutrition")

        #turn user input from pydantic into a dictionary
        input_dict = {
            "user": user_input.user,
            "pet_name": user_input.pet_name,
            "message": user_input.message,  # Changed from user_input.input to user_input.message
            "pet_type": user_input.pet_type,
            "pet_age": user_input.pet_age,
            "pet_lifestage": user_input.pet_lifestage,
            "pet_weight": user_input.pet_weight,
            "exercise_level": user_input.exercise_level
        }
        
        result = Vetai2().crew().kickoff(inputs=input_dict)
        print(result)

def kickoff():
    vet_flow = VetFlow()
    vet_flow.kickoff()


def plot():
    vet_flow = VetFlow()
    vet_flow.plot()


if __name__ == "__main__":
    kickoff()
