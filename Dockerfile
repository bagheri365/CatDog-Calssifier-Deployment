FROM python:3.8.3-slim

RUN apt-get update 
    
WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0" ]