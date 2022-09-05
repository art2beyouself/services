<b> Description</b> 

This repository contains a docker image that allows running API built using FastAPI.

<b> Build docker image</b> 

You can build this docker image from a dockerfile using this command

docker build -t art2beyouself/services:latest .

<b> Run the docker container</b> 

docker run -p 8000:8000 art2beyouself:latest
