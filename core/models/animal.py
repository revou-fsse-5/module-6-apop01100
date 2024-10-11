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
            
        date_format = "%d/%m/%Y"
            
        animal_dict = {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "birth": self.birth.strftime(date_format),
            "age": str(self.age) + year,
            "habitat": self.habitat,
            "data_records": {
                "created": self.created_date.strftime(date_format),
                "updated": self.update_date.strftime(date_format) if self.update_date else None
            }
            
        }
        
        return animal_dict
