
# One2n-Assignment
This folder conatins the solution for the bootcamp milestone-6. 

### Problem Statement:
Link for PS: https://one2n.notion.site/6-Setup-Kubernetes-cluster-075176deeaf34960be84ca026f59ce01

### Pre-Requisites:
* minikube 
* docker-desktop/virtualbox (I have used docker desktop to setup the k8s cluster but 
you can use virtualbox also) 
* kubectl

### How to start the multinode cluster using minikube 
Please make sure you have minikube & docker-desktop installed in you localhost 

```bash 
# To start the minikube with multinode cluster  
minikube start --nodes 3 -p on2n-sre-bootcamp 

# To stop the minikube k8s cluster 
minikube stop
```
Once the minikube cluster is up and running you can access it using the kubectl command.


### File Description:

* **k8s**: This folder contains the file nodes.yml which taints the k8s nodes.
