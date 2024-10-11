from core.models.animal import Animal
from datetime import datetime
from core.constant.messages import Messages

def str_to_date(string):
    return datetime.strptime(string, "%d/%m/%Y")

payload_post = {
        "name": "Paul",
        "species": "octopus",
        "birth": str_to_date("12/07/2019"),
        "gender": "male",
        "age": "5",
        "habitat": "coastal marine waters"
    }

payload_put = {
        "name": "Lily",
        "species": "elephant",
        "birth": str_to_date("29/05/2009"),
        "gender": "female",
        "age": "15",
        "habitat": "savanna"
    }

# TEST CODE
def test_get_animals(client, appjson, generate_fake_animal):
    response = client.get("/animals/", headers=appjson)
    message = response.json.get("message")
    
    assert response.status_code == 200
    assert message == "success GET animals data"
    
def test_success_get_animal_by_id(client, appjson, generate_fake_animal):
    response = client.get("/animals/1", headers=appjson)
    message = response.json["message"]
    animal_res = response.json["animal"]
    id = animal_res["id"]
    
    assert response.status_code == 200
    assert message == Messages.success_message("animal", "GET", id)
    
    animal_id = Animal.query.get(id)
    assert animal_id.id == id
    assert animal_id.name == animal_res["name"]
    assert animal_id.species == animal_res["species"]
    assert animal_id.birth == str_to_date(animal_res["birth"])
    assert animal_id.age == int(animal_res["age"][:2])
    assert animal_id.habitat == animal_res["habitat"]

def test_failed_get_animal_by_id(client, appjson, generate_fake_animal):
    id = 2
    response = client.get(f"/animals/{id}", headers=appjson) # id = 2 never exist in generate_fake_animal function
    message = response.json.get("message")
    
    assert response.status_code == 404
    assert message == Messages.not_found_messages("animal", id)
    
def test_success_add_user(client, appjson, test_db):
    # prsentation layer
    response = client.post("/animals/", headers=appjson, json=payload_post)
    
    # bussiness logic layer
    message = response.json["message"]
    id = response.json["animal"]["id"]
    assert response.status_code == 201
    assert message == Messages.success_message("animal", "POST", id)
    
    # data layer
    new_animal = Animal.query.get(id)
    assert new_animal.id == id
    assert new_animal.name == payload_post["name"]
    assert new_animal.species == payload_post["species"]
    assert new_animal.birth == payload_post["birth"]
    assert new_animal.age == int(payload_post["age"][:2])
    assert new_animal.habitat == payload_post["habitat"]
    
def test_update_animal_by_id(client, appjson, generate_fake_animal):
    id = 1
    response = client.put(f"/animals/{id}", headers=appjson, json=payload_put)
    
    message = response.json["message"]
    id = response.json["animal"]["id"]
    
    assert response.status_code == 200
    assert message == Messages.success_message("animal", "PUT", id)
    
    animal_by_id = Animal.query.get(id)
    assert animal_by_id.name == payload_put["name"]
    assert animal_by_id.species == payload_put["species"]
    assert animal_by_id.gender == payload_put["gender"]
    assert animal_by_id.birth == payload_put["birth"]
    assert animal_by_id.age == int(payload_put["age"][:2])
    assert animal_by_id.habitat == payload_put["habitat"]
    
def test_failed_update_animal_by_id(client, appjson, generate_fake_animal):
    id = 2
        
    response = client.put(f"/animals/{id}", headers=appjson, json=payload_put)
    message = response.json["message"]
    
    assert response.status_code == 404
    assert message == Messages.not_found_messages("animal", id)

def test_delete_animal_by_id(client, appjson, generate_fake_animal):
    id = 1
    response = client.delete(f"/animals/{id}", headers=appjson)
    message = response.json["message"]
    
    assert response.status_code == 200
    assert message == Messages.success_message("animal", "DELETE", id)
    
def test_failed_delete_animal_by_id(client, appjson, generate_fake_animal):
    id = 2
    response = client.delete(f"/animals/{id}", headers=appjson)
    message = response.json["message"]
    
    assert response.status_code == 404
    assert message == Messages.not_found_messages("animal", id)