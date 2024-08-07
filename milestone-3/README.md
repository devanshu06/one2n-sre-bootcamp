
# One2n-Assignment
This folder conatins the solution for the bootcamp milestone-3. 

### Problem Statement:
Link for PS: https://one2n.notion.site/3-Setup-one-click-local-development-setup-9dae469099b845938841144bf5f850ab

### Pre-Requisites:
To Run this Code on you local you need below things:
* docker & docker-compose 
* postman
* make

### How to start the docker container

To start the docker container we have run some make targets which will start our api and db containers.


```bash
# To start the docker container up and create a new build for the api containers
make up

# To stop the docker containers 
make down

# To start the Migration on your local machine: 
# Before running this make action Please keep in mind your database is up on your local and virtual Enviornment is being setup 
make run_db_migration

```

#### Note: 

If you want to change the Configuration of Database and the Database Schema Migration Please check the `docker-compose.yml` file.  
Description of Environment Variables in the docker-compose.yml file.  
*  Explanation of ENV varibale in the `api` service:  
    *  `DATABASE_HOST` #Provide the Database HostName/URL. Default is db (service name of db container)
    *  `DATABASE_USER` #Provide the Databse Username. Default is root
    *  `DATABASE_PASSWORD` #Provide the Database Password. Default is password
    *  `DATABASE_NAME` #Provide the Database Name. Default is studentdb
    *  `RUN_MIGRATION` # Provide the Boolean values for this TRUE/FALSE if you want to run the DB Schema Migration  
*  Explanation of ENV variable in the `db` service:  
    *  `MYSQL_ROOT_PASSWORD` #To setup the root password for the Database container. Default is password





