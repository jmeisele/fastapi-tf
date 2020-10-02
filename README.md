# FastAPI Tensorflow Image Recognition

A fast FastAPI (Get it?) by [Sebastián Ramírez](https://github.com/tiangolo) for image recognition using Tensorflow MobileNetV2.

## Requirements
Python 3.6+

## Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).
```bash
pip install -r requirements
``` 

## Run It
1. Start your  app with: 
```bash
uvicorn "app.main:app" --reload
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
      
3. You can use the sample image from the `images/goldenretriever.jpg` file when trying out the image prediction model using the API.
   ![goodboy](./images/goldenretriever.jpg)
