### Build image

`docker build -t mydatabasetest .`

### Show all images

`docker image ls`

### Run container

`docker run --rm --name mydatabase mydatabasetest:latest` 

### Show all running containers

`docker container ls`

### Init db (app specific)

`docker exec -it mydatabase flask --app app.py init-db`

### Run container with abs path as volume

`docker run --rm --name mydatabase -v ./data:/opt/code/source/data mydatabasetest:latest`

### Create docker volume and run container with new volume name

`docker volume create mydatabase`

`docker run --rm --name mydatabase -v mydatabase:/opt/code/source/data mydatabasetest:latest`

### Run container with exposed port

`docker run --rm --name mydatabase -v ./data:/opt/code/source/data -p 8080:8080 mydatabasetest:latest`
