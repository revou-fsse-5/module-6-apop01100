from flask import Flask, redirect
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

load_dotenv()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_CONNECTION_STRING")
    db.init_app(app)
    migrate.init_app(app, db)
    swagger = Swagger(app)
    
    @app.route("/")
    def index():
        return redirect("/apidocs/#/")
    
    with app.app_context():
        from core.routes.api import employee as employee_blueprint
        from core.routes.api import animal as animal_blueprint
        app.register_blueprint(employee_blueprint, url_prefix="/employees")
        app.register_blueprint(animal_blueprint, url_prefix="/animals")
    
    return app

    