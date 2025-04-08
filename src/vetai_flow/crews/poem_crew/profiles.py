from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Union
from datetime import datetime

class pet_profile(BaseModel):
        #store all pet profile information
        user: str = Field(..., description="The name of the pet owner")
        pet_type: str = Field(..., description="The type of the pet")
        pet_age: str = Field(..., description="The age of the pet")
        pet_lifestage: str = Field(..., description="The lifestage of the pet")
        pet_weight: str = Field(..., description="The weight of the pet")
        exercise_level: str = Field(..., description="The exercise level of the pet")
        message: str = Field(..., description="The message from the pet owner")

class nutrition_plan(BaseModel):
        # Basic information
        ME: float = Field(..., description="Metabolizable Energy in kcal/day")
        pet_lifestage: str = Field(..., description="Life stage of the pet (growth, adult, senior, breeding)")
        
        # Macronutrients
        crude_protein_min: float = Field(..., description="Minimum Crude Protein in g per day")
        crude_protein_max: Optional[float] = Field(None, description="Maximum Crude Protein in g per day")
        
        crude_fat_min: float = Field(..., description="Minimum Crude Fat in g per day")
        crude_fat_max: Optional[float] = Field(None, description="Maximum Crude Fat in g per day")
        
        linoleic_acid_min: float = Field(..., description="Minimum Linoleic Acid in g per day")
        linoleic_acid_max: Optional[float] = Field(None, description="Maximum Linoleic Acid in g per day")
        
        ALA_min: Optional[float] = Field(None, description="Minimum Alpha-Linolenic Acid in g per day")
        ALA_max: Optional[float] = Field(None, description="Maximum Alpha-Linolenic Acid in g per day")
        
        EPA_DHA_min: Optional[float] = Field(None, description="Minimum EPA + DHA in g per day")
        EPA_DHA_max: Optional[float] = Field(None, description="Maximum EPA + DHA in g per day")
        
        # Minerals
        calcium_min: float = Field(..., description="Minimum Calcium in g per day")
        calcium_max: Optional[float] = Field(None, description="Maximum Calcium in g per day")
        
        phosphorus_min: float = Field(..., description="Minimum Phosphorus in g per day")
        phosphorus_max: Optional[float] = Field(None, description="Maximum Phosphorus in g per day")
        
        potassium_min: float = Field(..., description="Minimum Potassium in g per day")
        potassium_max: Optional[float] = Field(None, description="Maximum Potassium in g per day")
        
        sodium_min: float = Field(..., description="Minimum Sodium in g per day")
        sodium_max: Optional[float] = Field(None, description="Maximum Sodium in g per day")
        
        chloride_min: float = Field(..., description="Minimum Chloride in g per day")
        chloride_max: Optional[float] = Field(None, description="Maximum Chloride in g per day")
        
        magnesium_min: float = Field(..., description="Minimum Magnesium in g per day")
        magnesium_max: Optional[float] = Field(None, description="Maximum Magnesium in g per day")
        
        iron_min: float = Field(..., description="Minimum Iron in mg per day")
        iron_max: Optional[float] = Field(None, description="Maximum Iron in mg per day")
        
        copper_min: float = Field(..., description="Minimum Copper in mg per day")
        copper_max: Optional[float] = Field(None, description="Maximum Copper in mg per day")
        
        manganese_min: float = Field(..., description="Minimum Manganese in mg per day")
        manganese_max: Optional[float] = Field(None, description="Maximum Manganese in mg per day")
        
        zinc_min: float = Field(..., description="Minimum Zinc in mg per day")
        zinc_max: Optional[float] = Field(None, description="Maximum Zinc in mg per day")
        
        iodine_min: float = Field(..., description="Minimum Iodine in mg per day")
        iodine_max: Optional[float] = Field(None, description="Maximum Iodine in mg per day")
        
        selenium_min: float = Field(..., description="Minimum Selenium in mg per day")
        selenium_max: Optional[float] = Field(None, description="Maximum Selenium in mg per day")
        
        # Vitamins
        vitamin_a_min: float = Field(..., description="Minimum Vitamin A in IU per day")
        vitamin_a_max: Optional[float] = Field(None, description="Maximum Vitamin A in IU per day")
        
        vitamin_d_min: float = Field(..., description="Minimum Vitamin D in IU per day")
        vitamin_d_max: Optional[float] = Field(None, description="Maximum Vitamin D in IU per day")
        
        vitamin_e_min: float = Field(..., description="Minimum Vitamin E in IU per day")
        vitamin_e_max: Optional[float] = Field(None, description="Maximum Vitamin E in IU per day")
        
        thiamine_min: float = Field(..., description="Minimum Thiamine in mg per day")
        thiamine_max: Optional[float] = Field(None, description="Maximum Thiamine in mg per day")
        
        riboflavin_min: float = Field(..., description="Minimum Riboflavin in mg per day")
        riboflavin_max: Optional[float] = Field(None, description="Maximum Riboflavin in mg per day")
        
        pantothenic_acid_min: float = Field(..., description="Minimum Pantothenic Acid in mg per day")
        pantothenic_acid_max: Optional[float] = Field(None, description="Maximum Pantothenic Acid in mg per day")
        
        niacin_min: float = Field(..., description="Minimum Niacin in mg per day")
        niacin_max: Optional[float] = Field(None, description="Maximum Niacin in mg per day")
        
        pyridoxine_min: float = Field(..., description="Minimum Pyridoxine in mg per day")
        pyridoxine_max: Optional[float] = Field(None, description="Maximum Pyridoxine in mg per day")
        
        folic_acid_min: float = Field(..., description="Minimum Folic Acid in mg per day")
        folic_acid_max: Optional[float] = Field(None, description="Maximum Folic Acid in mg per day")
        
        vitamin_b12_min: float = Field(..., description="Minimum Vitamin B12 in mg per day")
        vitamin_b12_max: Optional[float] = Field(None, description="Maximum Vitamin B12 in mg per day")
        
        choline_min: float = Field(..., description="Minimum Choline in mg per day")
        choline_max: Optional[float] = Field(None, description="Maximum Choline in mg per day")
        