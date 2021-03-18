from flask.cli import FlaskGroup

from search_svc import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()