Description
This repository contains a docker image that allows running API built using FastAPI.

Build docker image
You can build this docker image from a dockerfile using this command
docker build -t art2beyouself/services:latest .

Run the docker container
You can just run docker container
docker run -p 8000:8000 art2beyouself:latest
