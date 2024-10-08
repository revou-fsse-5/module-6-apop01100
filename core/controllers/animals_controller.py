from flask import request, jsonify
from core.DAL.animals_dal import AnimalDAL
from core.constant.messages import Messages

class AnimalsControllers:
    
    @staticmethod
    def get_animals():
        """
        file: ../constant/api_docs/animal/get_animals.yml
        """
        animals = AnimalDAL.get_animals()
        return jsonify({
            "message": Messages.success_message("animals", "GET"),
            "animals": [animal.to_dict() for animal in animals]
        }), 200
    
    @staticmethod
    def get_animal_by_id(id):
        """
        file: ../constant/api_docs/animal/get_animal_by_id.yml
        """
        animal = AnimalDAL.get_animal_by_id(id)
        if animal is not None:
            return jsonify({
                "message": Messages.success_message("animal", "GET", id),
                "animal": animal.to_dict()
            }), 200
        return jsonify({
            "message": Messages.not_found_messages("animal", id)
            }), 404
    
    @staticmethod
    def add_animal():
        """
        file: ../constant/api_docs/animal/add_animal.yml
        """
        data = request.json
        new_animal = AnimalDAL.add_animal(data)
        return jsonify({
            "message": Messages.success_message("animal", "POST", new_animal.get("id")),
            "animal": new_animal
        }), 201
        
    @staticmethod
    def update_animal(id):
        """
        file: ../constant/api_docs/animal/update_animal_by_id.yml
        """
        data = request.json
        updated_animal = AnimalDAL.update_animal(id, data)
        if updated_animal is not None:
            return jsonify({
                "message": Messages.success_message("animal", "PUT", id),
                "animal": updated_animal
            }), 200
        return jsonify({
            "message": Messages.not_found_messages("animal", id)
        }), 404
        
    @staticmethod
    def delete_animal(id):
        """
        file: ../constant/api_docs/animal/delete_animal_by_id.yml
        """
        delete_message = AnimalDAL.delete_animal(id)
        if delete_message is not None:
            return jsonify({
                "message": delete_message
            }), 200
        return jsonify({
            "message": delete_message
        }), 404