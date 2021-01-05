# Deployment of a Cat and Dog Image Classifier with Flask and Docker

In this repository, I share my practice in containerizing a Machine Learning (ML) model as REST API using Flask and Docker.

## Tools
- Python (Tensorflow & Pillow)
- Flask, HTML & CSS
- Docker

## About the ML model

The ML model consists of data preprocessing, feature extraction and classifier. In the training phase, data augmentation and dropouts techniques are utitlized to improve the performance. Below is the block diagram of the ML model.

<p align="center">
    <img src="https://github.com/bagheri365/CatDog-Calssifier-Deployment/blob/main/demo/ML_diagram.png">
</p>
<p align="center">
    Figure: Cat vs Dog Classifier diagram.
</p>


## About the Docker

#### Build a docker image

Build an image from the Dockerfile as the following:

```
docker build -t myimage:latest .
```

Note that a Docker Image is a template that contains the application, and all the dependencies required to run that application on Docker.

#### Run the docker container

You can run the docker container as the following:

```
docker run -it -p 5000:5000 myimage
```

Note that the container simply is running instance of the image.


## Demos

