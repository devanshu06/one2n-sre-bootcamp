
# One2n-Assignment
This folder conatins the solution for the bootcamp milestone-2. 

### Problem Statement:
Link for PS: https://one2n.notion.site/2-Containerise-REST-API-42ef56d543714557bae91cd254f00bbd

### Pre-Requisites:
To Run this Code on you local you need below things:
* python & pip >= 3.6
* mysql 5.x
* postman

### How to build the docker image

To build the docker images you should be inside the milestone-2 directory and run the below command. I have used my personal docker hub repository to push the docker image

```bash
# To build the images with docker command
docker build -t  dev06/one2n-sre-bootcamp:rest-api .

# To remove the images with docker command
docker rmi dev06/one2n-sre-bootcamp:rest-api

# To push the images with docker command
docker push dev06/one2n-sre-bootcamp:rest-api
```

```bash
# To Build image with the make target
make build_image

# To Remove image with the make target
make clean_image

# To Push image with the make target to docker hub
make push_image
```





