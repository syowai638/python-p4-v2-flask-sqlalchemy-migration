# seed.py
from models import db, Employee, Department
from app import app

with app.app_context():
    db.create_all()

    db.session.add(Employee(name="Kai Uri", salary=89000))
    db.session.add(Employee(name="Alena Lee", salary=125000))
    db.session.add(Department(name="Payroll", location="Building A, 4th Floor"))
    db.session.add(Department(name="Human Resources", location="Building C, 1st Floor"))

    db.session.commit()
    print("✅ Seeded the database!")
