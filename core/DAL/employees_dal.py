from core.models.employee import Employee
from core import db
from core.constant.messages import Messages

class EmployeeDAL:
    
    @staticmethod
    def get_employees():
        return Employee.query.all()
    
    @staticmethod
    def get_employee_by_id(id):
        return Employee.query.get(id)
    
    @staticmethod
    def add_employee(data):
        new_employee = Employee(
            name = data.get("name"),
            role = data.get("role").lower(),
            start_work = data.get("work_hour").get("start"),
            end_work = data.get("work_hour").get("end")
        )
        db.session.add(new_employee)
        db.session.commit()
        
        return new_employee.to_dict()
    
    @staticmethod
    def update_employee(id, data):
        employee: Employee = Employee.query.get(id)
        if employee is not None:
            employee.name = data.get("name", employee.name)
            employee.role = data.get("role", employee.role)
            employee.start_work = data.get("work_hour").get("start", employee.start_work)
            employee.end_work = data.get("work_hour").get("end", employee.end_work)
            db.session.commit()
            return employee.to_dict()
        return None
    
    @staticmethod
    def delete_employee(id):
        employee = Employee.query.get(id)
        if employee is not None:
            db.session.delete(employee)
            db.session.commit()
            return Messages.success_message("employee", "DELETE", id)
        return None
            
        