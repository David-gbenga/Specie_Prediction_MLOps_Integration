From python:3.12-slim

WORKDIR /app

COPY requirement.txt .

RUN python -m pip install --upgrade pip 
RUN python -m pip install -r requirement.txt

COPY .  .

EXPOSE 5001

CMD ["python", "app.py"]

# To build the Docker image, run the following command in the terminal:
# docker build -t my-python-app .
#To run the Docker container, use the following command:
# docker run -p 5001:5001 my-python-app
#You can test the API endpoint using the following command:
#Invoke-RestMethod -Uri "http://localhost:5001/predict" -Method POST -ContentType "application/json" -Body '{"features":[1,2,3,4]}'
