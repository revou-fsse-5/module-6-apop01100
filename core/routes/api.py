from flask import Blueprint
from core.controllers.animals_controller import AnimalsControllers
from core.controllers.employees_controller import EmployeeControllers

employee = Blueprint('employees', __name__)
animal = Blueprint("animals", __name__)

employee.add_url_rule("/", view_func=EmployeeControllers.get_employees, methods=["GET"])
employee.add_url_rule("/<int:id>", view_func=EmployeeControllers.get_employee_by_id, methods=["GET"])
employee.add_url_rule("/", view_func=EmployeeControllers.add_employee, methods=["POST"])
employee.add_url_rule("/<int:id>", view_func=EmployeeControllers.update_employee, methods=["PUT"])
employee.add_url_rule("/<int:id>", view_func=EmployeeControllers.delete_employee, methods=["DELETE"])

animal.add_url_rule("/", view_func=AnimalsControllers.get_animals, methods=["GET"])
animal.add_url_rule("/<int:id>", view_func=AnimalsControllers.get_animal_by_id, methods=["GET"])
animal.add_url_rule("/", view_func=AnimalsControllers.add_animal, methods=["POST"])
animal.add_url_rule("/<int:id>", view_func=AnimalsControllers.update_animal, methods=["PUT"])
animal.add_url_rule("/<int:id>", view_func=AnimalsControllers.delete_animal, methods=["DELETE"])