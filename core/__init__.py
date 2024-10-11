from flask import Flask, redirect
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

load_dotenv()
db = SQLAlchemy()
migrate = Migrate()

def create_app(test=False):
    app = Flask(__name__)
    
    if test:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("TESTING_POSTGRES_CONNECTION_URI")
    else:    
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_CONNECTION_URI")
        
    db.init_app(app)
    migrate.init_app(app, db)
    swagger = Swagger(app)
    
    if not test:
        @app.route("/")
        def index():
            return redirect("/apidocs/#/")
    
        
    
    with app.app_context():
        from core.routes.api import employee as employee_blueprint
        from core.routes.api import animal as animal_blueprint
        app.register_blueprint(employee_blueprint, url_prefix="/employees")
        app.register_blueprint(animal_blueprint, url_prefix="/animals")
    
    return app

    