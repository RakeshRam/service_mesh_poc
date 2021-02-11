from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60))
    author = db.Column(db.String(60))
    publisher = db.Column(db.String(60))
    is_available = db.Column(db.Boolean)

    def __repr__(self):
        return self.name
    