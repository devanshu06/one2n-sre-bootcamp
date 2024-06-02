
# One2n-Assignment
This folder conatins the solution for the bootcamp milestone-5. 

### Problem Statement:
Link for PS: https://one2n.notion.site/5-Deploy-REST-API-its-dependent-services-on-bare-metal-fb158d50bfdd4b5fb200098be5c741a9

### Pre-Requisites:
* vagrant 
* virtualbox 

### How to run the code using the make 
Please make sure you have vagrant & virtualbox installed in you localhost 

```bash 
# To start the vagrant box with the all the setup and docker-container up and runnig 
make vagrant_up

# To stop the vagrant box 
make vagrant_down

# To destroy the vagrant box
make vagrant_destroy
```
Once the vagrant box is up and running you can hit the API on port 8080 and it will work.

### File Description:

* **Vagrantfile** - Contains the code for setting up vagrant box 
* **pre-check.sh** - Containes the script for installing the dependency and starting up the container inside the vagrant box
* **docker-compose-vagrant.yml** - Contains the setup for containers with the nginx
* **nginx.conf** - Contains the nginx configurantion with the upstream configured for api containers
