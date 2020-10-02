"""
Author: Jason Eisele
Date: October 1, 2020
Email: jeisele@shipt.com
Scope: App for Tensorflow Doggo classifier
"""
from pydantic import BaseModel


class HousePredictionResult(BaseModel):
    median_house_value: int
    currency: str = "USD"
