from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate()
db = SQLAlchemy()
