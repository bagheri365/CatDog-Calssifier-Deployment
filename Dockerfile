FROM python:3.8.3-slim

RUN apt update && \
    apt -y install git && \
    git clone https://github.com/bagheri365/CatDog-Calssifier-Deployment.git mygit 
    
WORKDIR /app
# WORKDIR /usr/src/app

ADD . /app

RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000
CMD ["python", "app.py"]