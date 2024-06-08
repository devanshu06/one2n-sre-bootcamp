
# One2n-Assignment
This folder conatins the solution for the bootcamp milestone-10. 

### Problem Statement:
Link for PS: https://one2n.notion.site/10-Setup-an-observability-stack-d9a62e134051402f8a5457fe293a7aff
### Pre-Requisites:
* minikube 
* docker-desktop/virtualbox (I have used docker desktop to setup the k8s cluster but 
you can use virtualbox also) 
* kubectl
* helm
* Your application stack should be up and running

### How to start the multinode cluster using minikube 
Please make sure you have minikube & docker-desktop installed in you localhost and your application stack should be up and running

Below is the sequence in which we have to run the manifest files to get this Milestone code up and running.


* **namespace.yml**: Use this file to setup the Namespace for observability stack
```bash
kubectl apply -f namespace.yml
```
* **loki.yml**: Use this file to setup the Loki for Logging
```bash
kubectl apply -f loki.yml
```
* **helm.sh**: This file has the command to deploy the promtail using the helm chart
```bash
Note: This file is not a script to do the automated setup you have to copy and paste the command to do the setup. 
```
* **promtail-values.yml**: This File is used as the config file for the promtail helm 
* **prometheus.yml**: Use this file to deploy the promethus  
```bash
kubectl apply -f prometheus.yml
```
* **grafana.yml**: Use this file to deploy the grafana  
```bash
kubectl apply -f grafana.yml
```
* **db-exporter.yml**: Use this file to deploy the db-exporter but make sure to update the Database connection values with your configured values
```bash
kubectl apply -f db-exporter.yml
```
* **blackbox-exporter.yml**: Use this file to deploy the blackbox exporter 
```bash
kubectl apply -f blackbox-exporter.yml
```

Once everything is up and running you can access the services by port-forwarding to the specific ports
```bash
kubectl port-forward svc/prometheus-service -n monitoring-ns 9090:9090
```

## Screenshots of Grafana and prometheus to show the working of the code

1 - Datasource in the grafana for Loki and prometheus 
![plot](milestone-10/screenshots/Grafana-Datasource.png)

2 - Logs of application in the grafana using the Loki 
![plot](milestone-10/screenshots/Grafana-Loki.png)

3 - Prometheus Targets
![plot](milestone-10/screenshots/Prometheus-target.png)  