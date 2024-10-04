from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

load_dotenv()

app = Flask(__name__)
swagger = Swagger(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_CONNECTION_STRING")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
    