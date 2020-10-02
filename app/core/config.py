"""
Author: Jason Eisele
Date: October 1, 2020
Email: jeisele@shipt.com
Scope: App for Tensorflow Image classifier
"""
from starlette.config import Config

APP_VERSION = "1.0.0"
APP_NAME = "Tensorflow Image Recognition FastAPI"
API_PREFIX = "/api"

config = Config(".env")

IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)
