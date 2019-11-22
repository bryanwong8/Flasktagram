from app.config import *
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='./static')

app.config['SECRET_KEY'] = "9387f95ddfec0a647d73d8e62428dc38"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://doadmin:luo1jfgxti91kkbh@temporary-do-user-6246468-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require"
app.config['SQLALCHEMY_POOL_SIZE'] = 60000
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.posts.routes import posts

app.register_blueprint(posts)
