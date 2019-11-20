from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='./static')

app.config['SECRET_KEY'] = "9387f95ddfec0a647d73d8e62428dc38"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://lxbkhrux:OpNDrg2quANkLTzxMPsnlPmh4pjLf75K@isilo.db.elephantsql.com:5432/lxbkhrux"
app.config['SQLALCHEMY_POOL_SIZE'] = 60000
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.posts.routes import posts

app.register_blueprint(posts)
