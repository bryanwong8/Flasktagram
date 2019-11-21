import os
from dotenv import load_dotenv
from os.path import dirname, join

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

S3_BUCKET = os.environ.get('S3_BUCKET')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
