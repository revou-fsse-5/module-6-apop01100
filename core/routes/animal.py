from flask import Blueprint, request, jsonify
from ..config import setting
from ..models.animal import Animal

animal_router = Blueprint("animal", __name__, url_prefix="/animals")

@animal_router.route("", methods=["GET", "POST"])
@animal_router.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
def animal(id=None):
    if request.method == "GET":   
        response = []
        if id is None:
            animals: list[Animal] = Animal.query.all()
            for animal in animals:
                response.append(animal.to_dict())
            return jsonify({
                "message": "success get all animal data",
                "animals": response
            }), 200
        else:
            animal: Animal = Animal.query.get(id)
            if animal is None:
                return jsonify({"message": "animal not found"}), 400
            return jsonify(
                    {   
                        "message": f"success get data animal id {id}",
                        "animal": animal.to_dict()
                    }
            ), 200        

    if request.method == "POST":
        data = request.json
        name = data.get("name")
        species = data.get("species").lower()
        gender = data.get("gender").lower()
        birth = data.get("birth")
        age = data.get("age")
        habitat = data.get("habitat").lower()
        
        check = Animal.query.filter_by(name=name).first()
        if check is not None:
            return jsonify({"message": "animal name already exist"}), 400
        
        animal = Animal(
            name=name,
            species=species,
            gender=gender,
            birth=birth,
            age=age,
            habitat=habitat    
        )
        
        setting.db.session.add(animal)
        setting.db.session.commit()
        
        return jsonify({
            "message": "success post new animal data",
            "animal": animal.to_dict()
        }), 200
    
    if request.method == "PUT":
        animal: Animal = Animal.query.get(id)
        if id is None:
            return jsonify({"message": "animal id not exist"}), 400
        
        data = request.json
        new_name = data.get("name", animal.name)
        new_species = data.get("species", animal.species)
        new_gender = data.get("gender", animal.gender)
        new_birth = data.get("birth", animal.birth)
        new_age = data.get("age", animal.age)
        new_habitat = data.get("habitat", animal.habitat)
        
        animal.name = new_name
        animal.species = new_species
        animal.gender = new_gender
        animal.birth = new_birth
        animal.age = new_age
        animal.habitat = new_habitat
        
        setting.db.session.commit()
        
        return jsonify({
            "message": f"data id {id} success to update",
            "animal": animal.to_dict()
        })
    
    if request.method == "DELETE":
        if id is None:
            return jsonify({"message": "animal id not exist"}), 400
        
        animal_id: Animal = Animal.query.get(id)
        
        setting.db.session.delete(animal_id)
        setting.db.session.commit()
        
        animals: list[Animal] = Animal.query.all()
        response = []
        for animal in animals:
            response.append(animal.to_dict())
            
        return jsonify({
            "message": f"delete animal with id {id} success to delete data",
            "animals": response
            }), 200
        
    
    
    