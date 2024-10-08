from core import db
from datetime import datetime

class Animal(db.Model):
    __tablename__ = "animal"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    species = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(128), nullable=True)
    birth = db.Column(db.DateTime, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    habitat = db.Column(db.String(128), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime, onupdate=datetime.now)
    
    def to_dict(self):
        if int(self.age) <= 1:
            year = " year"
        else:
            year = " years"
            
        employee_dict = {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "birth": self.birth,
            "age": self.age + year,
            "habitat": self.habitat,
            "data_records": {
                "created": self.created_date,
                "updated": self.update_date
            }
            
        }
        
        return employee_dict
