from flask import Blueprint, request, jsonify
from ..config import setting
from ..models.employee import Employee

employee_router = Blueprint("employee", __name__, url_prefix="/employees")

@employee_router.route("", methods=["GET", "POST"])
@employee_router.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
def employee(id=None):    
    if request.method == "GET":   
        if id is None:
            response = []
            employees: list[Employee] = Employee.query.all()
            for employee in employees:
                response.append({
                    "id": employee.id,
                    "name": employee.name,
                    "role": employee.role,
                    "schedule": {
                        "start": f"{employee.start_work}",
                        "end": f"{employee.end_work}"
                    }
                })
            return jsonify({
                "message": "success get all employee data",
                "employees": response
            }), 200
        else:
            employee: Employee = Employee.query.get(id)
            if employee is None:
                return jsonify({"message": "employee not found"}), 400
            return jsonify(
                    {   
                        "message": f"success get data employee id={id}",
                        "employee": [{
                            "id": employee.id,
                            "name": employee.name,
                            "schedule": {
                                "start": employee.start_work,
                                "end": employee.end_work
                            }
                        }]
                    }
            ), 200        

    if request.method == "POST":
        data = request.json
        name = data.get("name")
        role = data.get("role").lower()
        start_work = data.get("schedule").get("start")
        end_work = data.get("schedule").get("end")
        
        employee = Employee(
            name=name,
            role=role,
            start_work=start_work,
            end_work=end_work  
        )
        
        setting.db.session.add(employee)
        setting.db.session.commit()
        
        return jsonify({
            "message": f"success post new employee data with",
            "employee": [{
                "id": employee.id,
                "name": employee.name,
                "role": employee.role,
                "schedule": {
                    "start": f"{employee.start_work}",
                    "end": f"{employee.end_work}"
                }
            }]
        }), 200
    
    if request.method == "PUT":
        if id is None:
            return jsonify({"message": f"employee id={id} not exist"}), 400
        
        employee: Employee = Employee.query.get(id)
        
        data = request.json
        new_name = data.get("name", employee.name)
        new_role = data.get("role", employee.role)
        new_start_work = data.get("schedule").get("start", employee.start_work)
        new_end_work = data.get("schedule").get("end", employee.end_work)
        
        employee.name = new_name
        employee.role = new_role
        employee.start_work = new_start_work
        employee.end_work = new_end_work
        
        setting.db.session.commit()
        
        return jsonify({
            "message": f"data id={id} success to update",
            "empoloyee": [{
                "id": employee.id,
                "name": employee.name,
                "role": employee.role,
                "schedule": {
                    "start": f"{employee.start_work}",
                    "end": f"{employee.end_work}"
                }
            }]
        })
    
    if request.method == "DELETE":
        if id is None:
            return jsonify({"message": f"employee id={id} not exist"}), 400
        
        employee: Employee = Employee.query.get(id)
        
        setting.db.session.delete(employee)
        setting.db.session.commit()
        
        employees: list[Employee] = Employee.query.all()
        response = []
        for employee in employees:
            response.append({
                    "id": employee.id,
                    "name": employee.name,
                    "role": employee.role,
                    "schedule": {
                        "start": f"{employee.start_work}",
                        "end": f"{employee.end_work}"
                    }
                })
            
        return jsonify({
            "message": f"delete animal with id={id} success to delete data",
            "employees": response
            }), 200