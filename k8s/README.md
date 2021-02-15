# Example Flask, Kubernetes and MySQL Implementation

Flask App Deployed in a Kubernetes(minikube) cluster.

## <u>Using Minikube(Local SetUp)</u>

```bash
minikube start
```

## <u>Deploy MySQL</u>

Component | Command
------------ | -------------
Secret | kubectl apply -f k8s\secret\mysql-srt.yaml
ConfigMap | kubectl apply -f k8s\config\mysql-cm.yaml
Volume | kubectl apply -f k8s\volumes\mysql-pv.yaml
Service | kubectl apply -f k8s\services\mysql-sv.yaml
Deployment | kubectl apply -f k8s\deployments\mysql-dp.yaml

<br/>

**Connect to MySQL:**

```bash
kubectl run -it --rm --image=mysql:5.7.22 --restart=Never mysql-client -- mysql -h db -proot
```

---

## <u>Deploy Flask App</u>

Component | Command
------------ | -------------
Service | kubectl apply -f k8s\services\services-app-sv.yaml
Deployment | kubectl apply -f k8s\deployments\services-app-dp.yaml
Default Migrations | kubectl apply -f k8s\jobs\migration.yaml

<br/>

**Connect to Flask app instance:**

```bash
kubectl exec --stdin --tty <POD-NAME> -- /bin/sh
```

**Get Application IP:**

```bash
kubectl get svc
```

Note: On local machine running minikube, run below command in seperate CMD prompt to get external ip

```bash
minikube tunnel
```

## <u>[Ingress](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/) (Not Working)</u>

**Enable the Ingress controller(Minikube):**

```bash
minikube addons enable ingress
```

Component | Command
------------ | -------------
Ingress | kubectl apply -f k8s\ingress\ingress.yaml

<br/>

**Get Application IP:**

```bash
kubectl get ingress
```
