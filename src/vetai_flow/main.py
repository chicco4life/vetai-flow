#!/usr/bin/env python
from random import randint
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from vetai_flow.crews.poem_crew.poem_crew import Vetai2
from crewai import Agent, Crew, Process, Task
from vetai_flow.tools.custom_tool import MECalculator,NutritionCalculator
from vetai_flow.crews.poem_crew.profiles import pet_profile,nutrition_plan

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
    user: str = "Fed"
    pet_name: str = "Dodo"
    pet_type: str = "Poodle"
    pet_age: int = 7
    pet_lifestage: Literal["puppy", "adult", "senior", "breeding"] = "adult"
    pet_weight: float = 3.3
    exercise_level: Literal["minimal", "low", "moderate", "high"] = "low"
    message: str = "no" #"I have a toy poodle, she is 7 years old, and 3.3kg. She has mild mitral valve regurgitation.  She is otherwise healthy. What supplement should she take and how much?"
    

class VetFlow(Flow[UserInput]):
    #initiate tools
    def __init__(self):
        super().__init__()
        self.me_calculator = MECalculator()
        self.nutrition_calculator = NutritionCalculator()

    @start()
    def get_user_input(self):
        print("Getting user input")

        # Collect user input
        """
        user = input("What is your name? ")
        pet_name = input("What is your pet's name? ")
        pet_type = input("What breed is your pet? ")
        pet_age = input("How old is your pet? ")
        pet_lifestage = input("What is your pet's life stage? ")
        pet_weight = input("How much does your pet weigh (in kg)? ")
        exercise_level = input("How much does your pet exercise? ")
        message = input("Anything else you want to tell me about your pet? ")
        """

        # Create UserInput object with both fieldsç
        self.user_input = UserInput() #this is to directly passs in hard coded values
        """
        self.user_input = UserInput(
            user=user,
            pet_name=pet_name,
            pet_type=pet_type,
            pet_age=pet_age,
            pet_lifestage=pet_lifestage if pet_lifestage else None,
            pet_weight=pet_weight,
            exercise_level=exercise_level if exercise_level else None,
            message=message
        )
        """

        return self.user_input

    @listen(get_user_input)
    def calculate_metabolism(self, user_input: UserInput):
        print("calculating metabolism")
        
        # Pass only the relevant data to the calculator
        metabolism = self.me_calculator.run(
        pet_weight=float(user_input.pet_weight),
        pet_lifestage=user_input.pet_lifestage,
        exercise_level=user_input.exercise_level
        )

        #store metabolism for later use
        self.metabolism = metabolism

        print(metabolism)
        return metabolism

    @listen(calculate_metabolism)
    def calculate_nutrition(self, metabolism):
        print("calculating nutrition")

        # Use the stored user_input to get pet_lifestage
        nutrition_plan = self.nutrition_calculator.run(
            ME=metabolism,
            pet_lifestage=self.user_input.pet_lifestage
        )

        print(nutrition_plan)
        return nutrition_plan

    @listen(calculate_nutrition)
    def create_report(self, nutrition_plan):
        print("creating final report")

        #turn user input from pydantic into a dictionary
        input_dict = {
            "user": self.user_input.user,
            "pet_name": self.user_input.pet_name,
            "message": self.user_input.message,  # Changed from user_input.input to user_input.message
            "pet_type": self.user_input.pet_type,
            "pet_age": self.user_input.pet_age,
            "pet_lifestage": self.user_input.pet_lifestage,
            "pet_weight": self.user_input.pet_weight,
            "exercise_level": self.user_input.exercise_level,

            #add metabolism and nutrition plan
            "metabolism": self.metabolism,
            "nutrition_plan": nutrition_plan
        }
        print('input is:',input_dict)
        # Save the input_dict to the flow state
    
        final_result = Vetai2().crew().kickoff(inputs=input_dict)
        print('final result is:',final_result)

def kickoff():
    vet_flow = VetFlow()
    vet_flow.kickoff()


def plot():
    vet_flow = VetFlow()
    vet_flow.plot()


if __name__ == "__main__":
    kickoff()
