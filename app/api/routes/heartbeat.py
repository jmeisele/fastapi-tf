"""
Author: Jason Eisele
Date: October 1, 2020
Email: jeisele@shipt.com
Scope: App for Tensorflow Doggo classifier
"""
from fastapi import APIRouter

from app.data_models.heartbeat import HearbeatResult

router = APIRouter()


@router.get("/heartbeat", response_model=HearbeatResult, name="heartbeat")
def get_hearbeat() -> HearbeatResult:
    heartbeat = HearbeatResult(is_alive=True)
    return heartbeat
