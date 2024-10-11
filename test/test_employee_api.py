from core.models.employee import Employee
from datetime import datetime
from core.constant.messages import Messages

def str_to_time(string):
    return datetime.strptime(string, "%H:%M:%S").time()

payload_post = {
        "name": "John doe",
        "role": "finance",
        "work_hour": {
                "start": "09:00",
                "end": "17:00"
            }
    }

payload_put = {
        "name": "John Wick",
        "role": "assassin",
        "work_hour": {
            "start": "00:00:00",
            "end": "23:59:00"
        }
    }

# TEST CODE
def test_get_employees(client, appjson, generate_fake_employee):
    response = client.get("/employees/", headers=appjson)
    message = response.json["message"]
    
    assert response.status_code == 200
    assert message == Messages.success_message("employees", "GET")
    
def test_success_get_employee_by_id(client, appjson, generate_fake_employee):
    response = client.get("/employees/1", headers=appjson)
    message_res = response.json["message"]
    employee_res = response.json["employee"]
    id = employee_res["id"]
    
    assert response.status_code == 200
    assert message_res == Messages.success_message("employee", "GET", id)
    
    employee = Employee.query.get(id)
    assert employee.id == id
    assert employee.name == employee_res["name"]
    assert employee.role == employee_res["role"]
    assert employee.start_work == str_to_time(employee_res["work_hour"]["start"])
    assert employee.end_work == str_to_time(employee_res["work_hour"]["end"])

def test_failed_get_employee_by_id(client, appjson, generate_fake_employee):
    id = 2
    response = client.get(f"/employees/{id}", headers=appjson) # id = 2 never exist in generate_fake_employee function
    message = response.json.get("message")
    
    assert response.status_code == 404
    assert message == Messages.not_found_messages("employee", id)
    
def test_success_add_employee(client, appjson, test_db):
    # prsentation layer
    response = client.post("/employees/", headers=appjson, json=payload_post)
    
    # bussiness logic layer
    message = response.json["message"]
    employee_res = response.json["employee"]
    id = employee_res["id"]
    assert response.status_code == 201
    assert message == Messages.success_message("employee", "POST", id)
    
    # data layer
    new_employee = Employee.query.get(id)
    assert new_employee.id == id
    assert new_employee.name == employee_res["name"]
    assert new_employee.role == employee_res["role"]
    assert new_employee.start_work == str_to_time(employee_res["work_hour"]["start"])
    assert new_employee.end_work == str_to_time(employee_res["work_hour"]["end"])
    
def test_update_animal_by_id(client, appjson, generate_fake_employee):
    id = 1
    response = client.put(f"/employees/{id}", headers=appjson, json=payload_put)
    message = response.json["message"]
    
    assert response.status_code == 200
    assert message == Messages.success_message("employee", "PUT", id)
    
    employee = Employee.query.get(id)
    assert employee.name == payload_put["name"]
    assert employee.role == payload_put["role"]
    assert employee.start_work == str_to_time(payload_put["work_hour"]["start"])
    assert employee.end_work == str_to_time(payload_put["work_hour"]["end"])
    
def test_failed_update_employee_by_id(client, appjson, generate_fake_employee):
    id = 2
    response = client.put(f"/employees/{id}", headers=appjson, json=payload_put)
    message = response.json["message"]
    
    assert response.status_code == 404
    assert message == Messages.not_found_messages("employee", id)

def test_delete_animal_by_id(client, appjson, generate_fake_employee):
    id = 1
    response = client.delete(f"/employees/{id}", headers=appjson)
    message = response.json["message"]
    
    assert response.status_code == 200
    assert message == Messages.success_message("employee", "DELETE", id)
    
def test_failed_delete_animal_by_id(client, appjson, generate_fake_employee):
    id = 2
    response = client.delete(f"/employees/{id}", headers=appjson)
    message = response.json["message"]
    
    assert response.status_code == 404
    assert message == Messages.not_found_messages("employee", id)