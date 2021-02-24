# Example Istio Implementation

Flask App Deployed in a Kubernetes(minikube) cluster with Istio Service Mesh.

## <u>Istio precheck</u>

```bash
istioctl x precheck
```

## <u>[Istio Profiles](https://istio.io/latest/docs/setup/additional-setup/config-profiles/)</u>

```bash
istioctl install --set profile=default
```

## <u>Check Pods</u>

```bash
kubectl -n istio-system get pods
istioctl proxy-status
```

## <u>Inject Istio to Pods</u>

```bash
kubectl label namespace default istio-injection=enabled
# Restart all pods to get sidecar injected
kubectl delete pods --all
```

## <u>Istio Gateway & VirtualService</u>

**Deploy V2 application and enable VirtualService**

Component | Command
------------ | -------------
Gateway | kubectl apply -f k8s\istio-gateway\gateway.yaml
VirtualService | kubectl apply -f k8s\istio-gateway\services-vs.yaml

## <u>Traffic Splits</u>

**Deploy V2 application and enable VirtualService**

Component | Command
------------ | -------------
Deployment & Service | kubectl apply -f k8s\deployments\services-app-dp-v2.yaml
VirtualService | kubectl apply -f k8s\istio-gateway\services-vs.yaml
