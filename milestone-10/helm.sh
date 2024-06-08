# helm command to install the promtail

helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install promtail grafana/promtail \
    --namespace monitoring-ns \
    -f promtail-values.yml

helm upgrade promtail grafana/promtail \
    --namespace monitoring-ns \
    -f promtail-values.yml

helm uninstall promtail \
    --namespace monitoring-ns
