from application import db
from application.models import Base


class PlantPest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))
    pest_id = db.Column(db.Integer, db.ForeignKey('pest.id'))
    plant_name = db.Column(db.String(144), nullable=True)
    pest_name = db.Column(db.String(144), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)                              
    

class Plant(Base):
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'),
        nullable=True) 
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    species_name = db.Column(db.String(144), nullable=True)                       
    
                       



    

    def __init__(self, name):
        self.name = name
        




        