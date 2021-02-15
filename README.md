# Flask Example Services Application

Example Flask Services App with REST, MySQL, Gunicorn+Nginx, Docker and Kubernetes to demonstrate Service Mesh and API Gateway.

## <u>Installation</u>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirments.txt.

From project root DIR run

## <u>Usage(Docker)</u>

```bash
set COMPOSE_CONVERT_WINDOWS_PATHS=1
docker-compose up --build
```

---

## <u>DB SetUp</u>

```bash
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```

---

## <u>Usage(Manual)</u>

Set-up Local Environment:

```bash
pip install -r requirements.txt
```

Start Local Server:

```bash
python core/main.py
```

---

## <u>Features</u>

* Demo Home page with REST integration.
  * App V1: `http://localhost:5000/`
  * App V2: `http://localhost:5001/`
* [Gunicorn](https://gunicorn.org/)(Application Server) + [Nginx](https://www.nginx.com/)(Web Server)
* App Integrated with Docker.
* App Integrated with Kubernetes.[Instructions](k8s/README.md)
* Istio Implementation.[Instructions](k8s/istio-gateway/README.md)

---

## License

[MIT](https://choosealicense.com/licenses/mit/)