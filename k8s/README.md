# Example Flask, Kubernetes and MySQL Implementation

Flask App Deployed in a Kubernetes(minikube) cluster.

## <u>Using Minikube(Local SetUp)</u>

```bash
minikube start --cpus 6 --memory 8192
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
Deployment V1 | kubectl apply -f k8s\deployments\services-app-dp.yaml
Deployment V2 | kubectl apply -f k8s/deployments/services-app-dp-v2.yaml
Default Migrations | kubectl apply -f k8s\jobs\migration.yaml

---

**Test Application inside Cluster(POD):**

Service | Port-Fowart | URL
------------ | ------------- | -------------
Deployment V1 | kubectl  port-forward svc/services-app-service -n default 5000 | http://localhost:5000/
Deployment V2 | kubectl  port-forward svc/services-app-service-v2 -n default 5001 | http://localhost:5001/

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

## <u>[Ingress](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)</u>

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

---

## <u>Auto-Scaling</u>

**Horizontal POD Autoscale(HPA)**

Enable metrics-server addon in minikube.

```bash
minikube addons enable metrics-server
```

**Set AutoScale Condition**

```bash
kubectl autoscale deployment services-app --cpu-percent=80 --min=1 --max=10
```

**Check HPA Metrics**

```bash
kubectl get hpa
```

**Get Node and Pod Metrics**

```bash
kubectl top nodes
kubectl top pods
```
