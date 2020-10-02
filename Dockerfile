FROM python:3.6-stretch
RUN pip install pipenv
COPY . ./app
WORKDIR /app
RUN pipenv install 
EXPOSE 3000
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=3000", "--workers=10"]