from core.db import db
from core.main import app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# python manager.py db --help
# python manager.py db init
# python manager.py db migrate
# python manager.py db upgrade

if __name__ == '__main__':
    manager.run()