# Refer to the official doc of hashicorp vault to setup vault using the helm in minikube 

# Link: https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-minikube-raft

# Please enable the storage-provisioner-rancher addons on the minikube so that you don't face issue in storage provisoning

# minikube addons enable storage-provisioner-rancher -p on2n-sre-bootcamp

#helm deploy command for hashicorp vault

helm install vault hashicorp/vault \
    --namespace vault-ns \
    --values helm-vault-raft-values.yml


helm upgrade vault hashicorp/vault \
    --namespace vault-ns \
    --values helm-vault-raft-values.yml


# helm uninstall vault --namespace vault-ns (Use this command if you need to uninstall the helm)

# Helm Conifguration commands after installation of hashicorp vault helm

kubectl exec vault-0 -n vault-ns \
    -- vault operator init \
    -key-shares=1 \
    -key-threshold=1 \
    -format=json > cluster-keys.json

jq -r ".unseal_keys_b64[]" cluster-keys.json

VAULT_UNSEAL_KEY=$(jq -r ".unseal_keys_b64[]" cluster-keys.json)

kubectl exec vault-0 -n vault-ns -- vault operator unseal $VAULT_UNSEAL_KEY

kubectl exec -ti vault-1 -n vault-ns -- vault operator raft join http://vault-0.vault-internal:8200

kubectl exec -ti vault-2 -n vault-ns -- vault operator raft join http://vault-0.vault-internal:8200

kubectl exec -ti vault-1 -n vault-ns -- vault operator unseal $VAULT_UNSEAL_KEY

kubectl exec -ti vault-2 -n vault-ns -- vault operator unseal $VAULT_UNSEAL_KEY

# how to store secret in vault 

jq -r ".root_token" cluster-keys.json

kubectl exec --stdin=true --tty=true vault-0 -n vault-ns -- /bin/sh

vault login # paste the root token here which you get using the jq command above

vault secrets enable -path=data kv

vault kv put data/mysql/student-api username="<Fill-this-place-with-original-value>" password="<Fill-this-place-with-original-value>"

vault kv get secret/mysql/student-api

exit 

# We are creating the secrets using the root token which have all the access but our application only need to read the values 

kubectl exec --stdin=true --tty=true vault-0 -n vault-ns -- /bin/sh

vault policy write external-secret-operator-policy - <<EOF
path "data/mysql/student-api" {
  capabilities = ["read"]
}
EOF

vault token create -policy="external-secret-operator-policy" 
# After executing this command it will provide a token as below plase copy that value and store it 
# we are going to use that value in setting up the External Secrets Operator(ESO) 

# After performing the above steps your vault should be up and running with the secrets stored in it.

# Provisioning of External Secrets Operator(ESO):
# Refer to this link if you face any problem in setting up ESO I have taken reference from here: https://earthly.dev/blog/eso-with-hashicorp-vault/

helm repo add external-secrets https://charts.external-secrets.io
helm repo update

helm install external-secrets external-secrets/external-secrets \
  --namespace external-secrets-ns \
  --set installCRDs=true

# helm uninstall external-secrets --namespace external-secrets-ns (Use this command if you need to uninstall the helm)

echo "<Provide the token which you have copied above>" | base64 --encode

#paste the encode token in the vault-token.yml file 

kubectl apply -f vault-token.yml

kubectl apply -f vault-secret-store.yml

kubectl apply -f external-secret.yml