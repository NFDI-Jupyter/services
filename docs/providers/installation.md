# Installation 


## Kubernetes
This section covers an example installation of the [JupyterHub Outpost service](https://artifacthub.io/packages/helm/jupyter-jsc/jupyterhub-outpost) via helm. 

### Requirements

A Kubernetes Cluster up and running.

### Preparations

We assume that the Outpost service will run in the `outpost` namespace. To authenticate the JupyterHub instance, we have to create a Kubernetes secret with username+password. 

```bash
OUTPOST_PASSWORD=$(uuidgen)

kubectl -n outpost create secret generic --from-literal=usernames=jupyterhub --from-literal=passwords=${OUTPOST_PASSWORD} outpost-users
```

> If you want to connect multiple JupyterHubs to one JupyterHub Outpost, you have to create a secret with semicolon-separated usernames and passwords.  
> `kubectl create secret generics --from-literal=usernames=one;two;three --from-literal=passwords=pw1;pw2;pw3 outpost-users`

An encryption key is necessary to ensure that the data in the database is encrypted.

```bash
SECRET_KEY=$(python3 -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())')

kubectl -n outpost create secret generic outpost-cryptkey --from-literal=secret_key=${SECRET_KEY}
```

### Configuration

You have to ask the administrator of all JupyterHubs you want to connect for their ssh-publickey. In this scenario, we're using NodePort as service types. JupyterHub must be able to reach the JupyterHub Outpost service at the ports `30080` (access to the Outpost API) and `30022` (access to ssh daemon for port-forwarding). You can configure the ports to your liking, or choose a different Service type.

> In this scenario, the communication between JupyterHub and JupyterHub Outpost will not be encrypted. Do not use this in production. You'll find an example with encryption below.

Helm values:
```bash
cat <<EOF >> outpost_values.yaml
# Name of database encryption key secret
cryptSecret: outpost-cryptkey
# Name of JupyterHub username+password secret
outpostUsers: outpost-users
# ssh-publickey of JupyterHub(s) to connect
sshPublicKeys:
  - restrict,port-forwarding,command="/bin/echo No commands allowed" $(cat jupyterhub-sshkey.pub)
# Kubernetes service for the Outpost API
service:
  type: NodePort
  ports:
    nodePort: 30080
# Kubernetes service for port-forwarding
servicessh:
  type: NodePort
  ports:
    nodePort: 30022
EOF
```

> Check out the available options for ssh public keys [here](https://manpages.debian.org/experimental/openssh-server/authorized_keys.5.en.html#AUTHORIZED_KEYS_FILE_FORMAT). At least port-forwarding must be allowed.

### Installation

```bash
# Add JupyterHub Outpost chart repository
helm repo add jupyter-jsc https://kaas.pages.jsc.fz-juelich.de/helm-charts/
helm repo update
# Install the JupyterHub Outpost chart in the `outpost` namespace
helm upgrade --install --create-namespace --version 1.0.6 --namespace outpost -f outpost_values.yaml outpost jupyter-jsc/jupyterhub-outpost
```

Ensure that everything is up and running. Double check that the ports 30080 and 30022 are reachable for JupyterHub.  
Contact the [Jupyter4NFDI administrators](../support.md) to let them know how to reach your JupyterHub Outpost.


## Encryption via ingress

When running JupyterHub Outpost in production, you should ensure a certain level of encryption. An easy way is to use an ingress controller with a certificate.
For this example we've installed [cert-manager with a let's encrypt issuer](https://artifacthub.io/packages/helm/cert-manager/cert-manager) and [ingress-nginx](https://artifacthub.io/packages/helm/ingress-nginx/ingress-nginx). If you already have a certificate, you will only need ingress-nginx.

This example is an addition to the examples above.

### Configuration

```bash
FLOATING_IP_SSH=<EXTERNAL_IP_FOR_SSH_ACCESS>
cat <<EOF >> outpost_remote_values_ingress.yaml
# Name of database encryption key secret
cryptSecret: outpost-cryptkey
# Name of JupyterHub username+password secret
outpostUsers: outpost-users
# ssh-publickey of JupyterHub(s) to connect
sshPublicKeys:
  - restrict,port-forwarding,command="/bin/echo No commands allowed" $(cat jupyterhub-sshkey.pub)
# Kubernetes service for port-forwarding
servicessh:
  type: LoadBalancer
  loadBalancerIP: ${FLOATING_IP_SSH}
# Use ingress with TLS instead of a Kubernetes service for the Outpost API
ingress:
  enabled: true
  # Annotations for using LetsEncrypt as a certificate issuer
  annotations:
    acme.cert-manager.io/http01-edit-in-place: "true"
    cert-manager.io/cluster-issuer: letsencrypt-cluster-issuer
  hosts:
  - myremoteoutpost.com
  tls:
  - hosts:
    - myremoteoutpost.com
    # If using LetsEncrypt, the secret will be created automatically. Otherwise, please ensure the secret exists.
    secretName: outpost-tls-certmanager
EOF
```

JupyterHub will now be able to reach the JupyterHub Outpost API at `https://myremoteoutpost.com/services` and the ssh daemon for port-forwarding at `${FLOATING_IP_SSH}` on port 22.
Contact the [Jupyter4NFDI administrators](../support.md) to inform them about the new addresses.