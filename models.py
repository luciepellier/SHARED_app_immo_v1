from api import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)

class Contract(db.Model):
    __tablename__ = 'contracts'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    agency = db.Column(db.String(100), nullable = False)
    occupant = db.Column(db.String(100), nullable = False)
    apartment = db.Column(db.String(100), nullable = False)
    entry_date = db.Column(db.DateTime, default = datetime.utcnow, nullable = False)
    entry_inventory = db.Column(db.bool, nullable = False)
    deposit_payment = db.Column(db.Float, nullable = False)
    exit_date = db.Column(db.DateTime, default = datetime.utcnow)
    exit_inventory = db.Column(db.bool)

#method to represent the class object as a string
    def __repr__(self):
        return f"<Contract {self.name}>"