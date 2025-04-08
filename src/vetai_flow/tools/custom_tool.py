from crewai.tools import BaseTool
from typing import Type
from vetai_flow.crews.poem_crew.profiles import BaseModel, Field

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

class MECalculator(BaseTool):
    name: str = "ME Calculator"
    description: str = "Use the ME Calculator to calculate a pet's daily metabolism given their age, life stage, and weight"
    #args_schema: Type[BaseModel] = MyCustomToolInput
    def _run(self, pet_weight: float, pet_lifestage: str, exercise_level: str) -> float:
        # Define the life stage factors and exercise multipliers
        lifestage_factors = {
            "growth": 2.5,
            "adult": 1.6,
            "senior": 1.2,
            "breeding": 2.0
        }

        exercise_factors = {
            "minimal": 1.0,
            "low": 1.2,
            "moderate": 1.4,
            "high": 1.6
        }

        # Normalize the lifestage input to lower case and find the factor
        life_stage_key = pet_lifestage.lower()
        if life_stage_key not in lifestage_factors:
            raise ValueError("Invalid life stage provided")
        factor = lifestage_factors[life_stage_key]

        # Normalize the exercise level input to lower case and find the factor
        exercise_level_key = exercise_level.lower()
        if exercise_level_key not in exercise_factors:
            raise ValueError("Invalid exercise level provided")
        multiplier = exercise_factors[exercise_level_key]

        # Calculate the Metabolizable Energy (ME)
        ME = 70 * (pet_weight ** 0.75) * factor * multiplier
        print(f"The calculated ME is {ME}, where weight={pet_weight}, lifestage={pet_lifestage} & lifestafe factor={factor}, exercise={exercise_level} & exercise multiplier={multiplier}")
        return ME
    
class NutritionCalculator(BaseTool):
    name: str = "Nutrition Calculator"
    description: str = "Use the ME value and pet_lifestage to calculate the minimum and maximum nutrient intakes for a pet"
    #args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, ME:float, pet_lifestage:str)-> dict:  
        # Nutrient table: values per 1000 kcal ME.
        nutrient_table = {
            "Crude Protein": {
                "growth": {"min": 56.3, "max": None, "unit": "g"},
                "adult":  {"min": 45.0, "max": None, "unit": "g"}
            },
            "Crude Fat": {
                "growth": {"min": 21.3, "max": None, "unit": "g"},
                "adult":  {"min": 13.8, "max": None, "unit": "g"}
            },
            "Linoleic Acid": {
                "growth": {"min": 3.3, "max": None, "unit": "g"},
                "adult":  {"min": 2.8, "max": None, "unit": "g"}
            },
            "ALA": {
                "growth": {"min": 0.2, "max": None, "unit": "g"},
                "adult":  {"min": None, "max": None, "unit": "g"}  # Not determined (ND)
            },
            "EPA + DHA": {  # Eicosapentaenoic + Docosahexaenoic Acid
                "growth": {"min": 0.1, "max": None, "unit": "g"},
                "adult":  {"min": None, "max": None, "unit": "g"}  # ND
            },
            # Minerals
            "Calcium": {
                "growth": {"min": 3.0, "max": 6.25, "unit": "g"},
                "adult":  {"min": 1.25, "max": 4.5,  "unit": "g"}
            },
            "Phosphorus": {
                "growth": {"min": 2.5, "max": 4.0, "unit": "g"},
                "adult":  {"min": 1.0, "max": None, "unit": "g"}
            },
            "Potassium": {
                "growth": {"min": 1.5, "max": None, "unit": "g"},
                "adult":  {"min": 1.5, "max": None, "unit": "g"}
            },
            "Sodium": {
                "growth": {"min": 0.80, "max": None, "unit": "g"},
                "adult":  {"min": 0.20, "max": None, "unit": "g"}
            },
            "Chloride": {
                "growth": {"min": 1.10, "max": None, "unit": "g"},
                "adult":  {"min": 0.30, "max": None, "unit": "g"}
            },
            "Magnesium": {
                "growth": {"min": 0.15, "max": None, "unit": "g"},
                "adult":  {"min": 0.15, "max": None, "unit": "g"}
            },
            "Iron": {
                "growth": {"min": 22, "max": None, "unit": "mg"},
                "adult":  {"min": 10, "max": None, "unit": "mg"}
            },
            "Copper": {
                "growth": {"min": 3.1, "max": None, "unit": "mg"},
                "adult":  {"min": 1.83, "max": None, "unit": "mg"}
            },
            "Manganese": {
                "growth": {"min": 1.8, "max": None, "unit": "mg"},
                "adult":  {"min": 1.25, "max": None, "unit": "mg"}
            },
            "Zinc": {
                "growth": {"min": 25, "max": None, "unit": "mg"},
                "adult":  {"min": 20, "max": None, "unit": "mg"}
            },
            "Iodine": {
                "growth": {"min": 0.25, "max": 2.75, "unit": "mg"},
                "adult":  {"min": 0.25, "max": None, "unit": "mg"}
            },
            "Selenium": {
                "growth": {"min": 0.09, "max": 0.5, "unit": "mg"},
                "adult":  {"min": 0.08, "max": None, "unit": "mg"}
            },
            # Vitamins
            "Vitamin A": {
                "growth": {"min": 1250, "max": 62500, "unit": "IU"},
                "adult":  {"min": 1250, "max": 62500, "unit": "IU"}
            },
            "Vitamin D": {
                "growth": {"min": 125, "max": 750, "unit": "IU"},
                "adult":  {"min": 125, "max": 750, "unit": "IU"}
            },
            "Vitamin E": {
                "growth": {"min": 12.5, "max": None, "unit": "IU"},
                "adult":  {"min": 12.5, "max": None, "unit": "IU"}
            },
            "Thiamine": {
                "growth": {"min": 0.56, "max": None, "unit": "mg"},
                "adult":  {"min": 0.56, "max": None, "unit": "mg"}
            },
            "Riboflavin": {
                "growth": {"min": 1.3, "max": None, "unit": "mg"},
                "adult":  {"min": 1.3, "max": None, "unit": "mg"}
            },
            "Pantothenic Acid": {
                "growth": {"min": 3.0, "max": None, "unit": "mg"},
                "adult":  {"min": 3.0, "max": None, "unit": "mg"}
            },
            "Niacin": {
                "growth": {"min": 3.4, "max": None, "unit": "mg"},
                "adult":  {"min": 3.4, "max": None, "unit": "mg"}
            },
            "Pyridoxine": {
                "growth": {"min": 0.38, "max": None, "unit": "mg"},
                "adult":  {"min": 0.38, "max": None, "unit": "mg"}
            },
            "Folic Acid": {
                "growth": {"min": 0.054, "max": None, "unit": "mg"},
                "adult":  {"min": 0.054, "max": None, "unit": "mg"}
            },
            "Vitamin B12": {
                "growth": {"min": 0.007, "max": None, "unit": "mg"},
                "adult":  {"min": 0.007, "max": None, "unit": "mg"}
            },
            "Choline": {
                "growth": {"min": 340, "max": None, "unit": "mg"},
                "adult":  {"min": 340, "max": None, "unit": "mg"}
            }
        }
    
        # Determine which stage to use.
        # Use "growth" for "growth" and "breeding"; use "adult" for "adult" and "senior".
        stage = None
        if pet_lifestage.lower() in ["growth", "breeding"]:
            stage = "growth"
        elif pet_lifestage.lower() in ["adult", "senior"]:
            stage = "adult"
        else:
            raise ValueError("Invalid lifestage.")
        
        # Factor to scale per 1000 kcal values to the dog's daily ME.
        factor = ME / 1000.0
        
        # Calculate daily nutrient intake for each nutrient.
        results = {}
        for nutrient, stages in nutrient_table.items():
            min_val = stages[stage]["min"]
            max_val = stages[stage]["max"]
            unit = stages[stage]["unit"]
            
            calculated_min = factor * min_val if min_val is not None else None
            calculated_max = factor * max_val if (max_val is not None) else None
            
            results[nutrient] = {
                "min_intake": calculated_min,
                #"max_intake": calculated_max,
                "unit": unit
            }
        
        return results