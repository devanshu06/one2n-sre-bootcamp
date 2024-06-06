
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

Below is the sequence in which we have to run the manifest files to get this Milestone code up and running.

* **ns.yml**: Use this file to create the namespace in the K8s 
```bash
kubectl apply -f ns.yml
```
* **nodes.yml**: Use this file to taint the nodes 
```bash
kubectl apply -f nodes.yml
```
* **helm.sh**: Use file to setup the HashiCorp Vault and ESO.
```bash
Note: This file is not a script to do the automated setup you have to copy and paste the command and run one by one to do the setup. 
```
* **helm-vault-raft-values.yml**: This File is used as the config file for the vault helm 
* **vault-secret-store.yml**: This file contains the configuration for ESO to connect with the Valut Server
```bash
kubectl apply -f vault-secret-store.yml
```
* **external-secret.yml**: This file will connect to the vault and create a secret in the student-api ns which can be used by our database.
```bash
kubectl apply -f external-secret.yml
```
* **database.yml**: Use this manifest file to make the database pod up 
```bash
kubectl apply -f database.yml
```
* **application.yml**: Use this manifest file to make the rest-api pod up 
```bash
kubectl apply -f application.yml
```


Once everything is up and running you can access it by port-forwarding the rest-api svc on port 5000:5000 to acces it 
```bash
kubectl port-forward svc/api-server-svc -n student-api 5000:5000
```


### File Description:

* **k8s**: This folder contains the files which is used to complete the milestone-7
* **k8s/readme.md**: This file contains the explanation of each manifest and the link which I followed to do the setup of Hashicorp Vault and ESO using helm.
