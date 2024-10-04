from flask import jsonify
from core.routes.animal import animal_router
from core.routes.employee import employee_router
from core.config import setting

app = setting.app

app.register_blueprint(animal_router)
app.register_blueprint(employee_router)