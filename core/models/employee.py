from core import db

class Employee(db.Model):
    __tablename__ = "employee"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), nullable=False)
    start_work = db.Column(db.Time,  nullable=False)
    end_work = db.Column(db.Time, nullable=False)
    
    def to_dict(self):
        employee_dict = {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "work_hour": {
                "start": f"{self.start_work}",
                "end": f"{self.end_work}"
            }
        }
        
        return employee_dict
