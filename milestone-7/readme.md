# One2n-Assignment
This folder conatins the solution for the bootcamp milestone-7. 

### Problem Statement:
Link for PS: https://one2n.notion.site/7-Deploy-REST-API-its-dependent-services-in-K8s-e340500617354f4680211c6ff2915e21

### Pre-Requisites:
* minikube 
* docker-desktop/virtualbox (I have used docker desktop to setup the k8s cluster but 
you can use virtualbox also) 
* kubectl
* helm

### How to start the multinode cluster using minikube 
Please make sure you have minikube & docker-desktop installed in you localhost 

```bash 
# To start the minikube with multinode cluster which we have created in the milestone-6 
minikube start -p on2n-sre-bootcamp 

# To stop the minikube k8s cluster 
minikube stop -p on2n-sre-bootcamp
```
Once the minikube cluster is up and running you can access it using the kubectl command.


### File Description:

* **k8s**: This folder contains the files which is used to complete the milestone-7
* **k8s/readme.md**: This file contains the explanation of each manifest and the link which I followed to do the setup of Hashicorp Vault and ESO using helm.