from flask.cli import FlaskGroup

from email_svc import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()