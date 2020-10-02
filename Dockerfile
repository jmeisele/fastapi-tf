FROM python:3.6-stretch
COPY . ./app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=3000", "--workers=10"]