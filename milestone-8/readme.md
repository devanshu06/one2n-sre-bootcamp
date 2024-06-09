
# One2n-Assignment
This folder conatins the solution for the bootcamp milestone-8. 

### Problem Statement:
Link for PS: https://one2n.notion.site/8-Deploy-REST-API-its-dependent-services-using-Helm-Charts-f6f12f8ee7de48c4b473fb799d16fb34
### Pre-Requisites:
* minikube 
* docker-desktop/virtualbox (I have used docker desktop to setup the k8s cluster but 
you can use virtualbox also) 
* kubectl
* helm
 
### How to start the multinode cluster using minikube 
Please make sure you have minikube & docker-desktop installed in you localhost.

Below is the sequence in which we have to run the manifest files to get this Milestone code up and running.


* **application-stack**: This folder contains the helm chart to deploy the application with the database 

* **application-stack/values.yaml**: This file contains all the values for the charts to be Up and running. 
```bash
#Command to install the helm chart 
helm install student-application application-stack \ 
    --namespace student-api \
    --values application-stack/values.yml

# Command to upgrade the helm chart 
helm upgrade student-application application-stack \ 
    --namespace student-api \
    --values application-stack/values.yml

# Command to delete the helm charts
helm uninstall student-application \ 
    --namespace student-api 
```