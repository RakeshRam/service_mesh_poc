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

---

## <u>Istio Addons</u>

```bash
kubectl apply -f /path/to/istio/folder(EX: istio-1.9.0)/samples/addons/
kubectl get svc -n istio-system
```

Addon  | Description
------------ | -------------
Prometheus | Monitoring System
Kiali |  Observability Dashboard for Istio
Grafana | Observability Dashboard for Istio
Tracing | Reporting of trace spans for workload-to-workload communications within a mesh
Jaeger | End to End distributed tracing system

</br>

## <u>Istio Gateway & VirtualService</u>

Component | Command
------------ | -------------
Gateway | kubectl apply -f k8s\istio-gateway\gateway.yaml

**Enable ExternalIP to Istio Ingress:**

```bash
kubectl get svc -n istio-system -l app=istio-ingressgateway
minikube tunnel -c
```

---

## <u>Traffic Splits</u>

**Deploy V2 application and enable VirtualService**

Component | Command
------------ | -------------
VirtualService | kubectl apply -f k8s/istio-gateway/traffic-splits/ts.yaml

---

## <u>Canary Deployment</u>

Component | Command
------------ | -------------
VirtualService | kubectl apply -f k8s/istio-gateway/canary/cn.yaml

---

## <u>Auto-Retry</u>

Component | Command
------------ | -------------
Deployment V3 | kubectl apply -f k8s\deployments\services-app-dp-v3.yaml
VirtualService | k8s/istio-gateway/retry/rt.yaml

---

## <u>Authentication & AuthorizationPolicy</u>

Component | Command
------------ | -------------
RequestAuthentication & AuthorizationPolicy | kubectl apply -f k8s\security\auth.yaml

---