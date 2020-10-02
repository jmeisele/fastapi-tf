"""
Author: Jason Eisele
Date: October 1, 2020
Email: jeisele@shipt.com
Scope: App for Tensorflow Image classifier
"""
from fastapi import APIRouter, UploadFile, File
from starlette.requests import Request
from PIL import Image
from io import BytesIO


# ML Model object itself
from app.services.models import DoggoModel
router = APIRouter()

def read_image_file(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

@router.post('/image')
async def predict_image(request: Request, file: UploadFile=File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg,jpeg or png format"
    else:
        model: DoggoModel = request.app.state.model
        image = read_image_file(await file.read())
        prediction = model.predict(image)
        return prediction
