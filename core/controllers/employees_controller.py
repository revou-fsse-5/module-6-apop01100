from flask import request, jsonify
from core.DAL.employees_dal import EmployeeDAL
from core.constant.messages import Messages

class EmployeeControllers:
    
    @staticmethod
    def get_employees():
        """
        file: ../constant/api_docs/employee/get_employees.yml
        """
        employees = EmployeeDAL.get_employees()
        return jsonify({
            "message": Messages.success_message("employees", "GET"),
            "employees": [employee.to_dict() for employee in employees]
        }), 200
    
    @staticmethod
    def get_employee_by_id(id):
        """
        file: ../constant/api_docs/employee/get_employee_by_id.yml
        """
        employee = EmployeeDAL.get_employee_by_id(id)
        if employee is not None:
            return jsonify({
                "message": Messages.success_message("employee", "GET", id),
                "employee": employee.to_dict()
            }), 200
        return jsonify({
            "message": Messages.not_found_messages("employee", id)
            }), 404
    
    @staticmethod
    def add_employee():
        """
        file: ../constant/api_docs/employee/add_employee.yml
        """
        data = request.json
        new_employee = EmployeeDAL.create_employee(data)
        return jsonify({
            "message": Messages.success_message("employee", "POST", new_employee.get("id")),
            "employee": new_employee
        }), 201
        
    @staticmethod
    def update_employee(id):
        """
        file: ../constant/api_docs/employee/update_employee_by_id.yml
        """
        data = request.json
        updated_employee = EmployeeDAL.update_employee(id, data)
        if updated_employee is not None:
            return jsonify({
                "message": Messages.success_message("employee", "PUT", id),
                "employee": updated_employee
            }), 200
        return jsonify({
            "message": Messages.not_found_messages("employee", id)
        }), 404
        
    @staticmethod
    def delete_employee(id):
        """
        file: ../constant/api_docs/employee/delete_employee_by_id.yml
        """
        delete_message = EmployeeDAL.delete_employee(id)
        if delete_message is not None:
            return jsonify({
                "message": delete_message
            }), 200
        return jsonify({
            "message": delete_message
        }), 404