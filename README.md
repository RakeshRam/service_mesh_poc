# Flask Example Services Application

Example Flask Services App with REST, MySQL, Docker and Kubernetes to demonstrate Service Mesh and API Gateway.

## <u>Installation</u>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirments.txt.

From project root DIR run

## <u>Usage(Docker)</u>

```bash
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

* Demo Home page.
  * `http://localhost:5000/`
* App Integrated with Docker.
* App Integrated with Kubernetes.[Instructions](k8s/README.md)

---

## License

[MIT](https://choosealicense.com/licenses/mit/)