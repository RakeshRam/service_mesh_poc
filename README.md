# Flask Example Services Application

Example Flask Services App with REST, MySQL, Gunicorn+Nginx, Docker and Kubernetes to demonstrate Service Mesh and API Gateway.

## <u>Installation</u>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirments.txt.

From project root DIR run

## <u>Usage(Docker)</u>

```bash
docker-compose up --build
```

---

## <u>Features</u>

* Demo Home page with REST integration.
  * App V1: `http://localhost:5000/`
  * App V2: `http://localhost:5001/`
* [Gunicorn](https://gunicorn.org/)(Application Server) + [Nginx](https://www.nginx.com/)(Web Server)
* App Integrated with Docker.
* App Integrated with Kubernetes.[Instructions](k8s/README.md)
* Istio Implementation.[Instructions](k8s/istio/README.md)

---

## License

[MIT](https://choosealicense.com/licenses/mit/)