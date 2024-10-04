from ..config.setting import db
from sqlalchemy_serializer import SerializerMixin

class Employee(db.Model, SerializerMixin):
    __tablename__ = "employee"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), nullable=False)
    start_work = db.Column(db.Time,  nullable=False)
    end_work = db.Column(db.Time, nullable=False)
