import pytest
from dotenv import load_dotenv
from core import create_app, db
from core.models.animal import Animal
from core.models.employee import Employee

load_dotenv()

@pytest.fixture
def app():
    app = create_app(test=True)
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client
            
@pytest.fixture
def test_db(app):
    db.create_all()
    
    yield db
    
    db.session.remove()
    db.drop_all()

@pytest.fixture
def generate_fake_animal(test_db):
    animal = Animal(name="Simba", 
                species="lion",
                age="12",
                gender="male",
                birth="05/29/2012", 
                habitat="savanna")
    test_db.session.add(animal)

    test_db.session.commit()
    
@pytest.fixture
def generate_fake_employee(test_db):
    employee = Employee(name="Alicia Johnson",
                     role="zookeeper",
                     start_work="09:00",
                     end_work="17:00")
    test_db.session.add(employee)
    
    test_db.session.commit()


@pytest.fixture
def appjson() -> dict:
    return {"Content-Type": "application/json"}