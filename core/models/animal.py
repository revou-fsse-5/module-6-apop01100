from ..config.setting import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class Animal(db.Model, SerializerMixin):
    __tablename__ = "animal"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    species = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(128), nullable=True)
    birth = db.Column(db.DateTime, nullable=True)
    age = db.Column(db.String(128), nullable=True)
    habitat = db.Column(db.String(128), nullable=True)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime, onupdate=datetime.now)
