"""
Author: Jason Eisele
Date: October 1, 2020
Email: jeisele@shipt.com
Scope: App for Tensorflow Doggo classifier
"""
from fastapi import APIRouter
from app.api.routes import heartbeat, prediction

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(prediction.router, tags=["prediction"], prefix="/predict")