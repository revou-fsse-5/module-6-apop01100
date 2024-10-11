from core.models.animal import Animal
from core import db
from core.constant.messages import Messages
from datetime import datetime

class AnimalDAL:
    
    @staticmethod
    def get_animals():
        return Animal.query.all()
    
    @staticmethod
    def get_animal_by_id(id):
        return Animal.query.get(id)
    
    @staticmethod
    def add_animal(data):
        new_animal = Animal(
            name = data.get("name"),
            species = data.get("species").lower(),
            gender = data.get("gender").lower() if data.get("gender") else None,
            birth = data.get("birth"),
            age = data.get("age"),
            habitat = data.get("habitat").lower()
        )
        db.session.add(new_animal)
        db.session.commit()
        
        return new_animal.to_dict()
    
    @staticmethod
    def update_animal(id, data):
        animal: Animal = Animal.query.get(id)
        if animal is not None:
            animal.name = data.get("name", animal.name)
            animal.species = data.get("species", animal.species)
            animal.gender = data.get("gender", animal.gender)
            animal.birth = data.get("birth", animal.birth)
            animal.age = data.get("age", animal.age)
            animal.habitat = data.get("habitat", animal.habitat)
            db.session.commit()
            return animal.to_dict()
        return None
    
    @staticmethod
    def delete_animal(id):
        animal = Animal.query.get(id)
        if animal is not None:
            db.session.delete(animal)
            db.session.commit()
            return Messages.success_message("animal", "DELETE", id)
        return None
            
        