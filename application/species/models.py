from application import db
from application.models import Base
from sqlalchemy.sql import text


class Species(Base):

    __tablename__ = "species"

    
    genus = db.Column(db.String(144), nullable=False)
    epithet = db.Column(db.String(144), nullable=False)
    water = db.Column(db.String(144), nullable=False)
    light = db.Column(db.String(144), nullable=False)
    plants = db.relationship('Plant', backref='plant_species', lazy=True)




    def __init__(self, genus, epithet, name, water, light):
        self.genus = genus
        self.epithet = epithet
        self.name = name
        self.water = water
        self.light = light


    def get_id(self):
        return self.id    


    @staticmethod
    def find_current_species():
        stmt = text("SELECT Species.id, Species.name FROM Species"
                     " LEFT JOIN Plant ON Plant.species_id = Species.id"
                     " LEFT JOIN Account ON Account.id = Plant.account_id"
                     " GROUP BY Account.id;")
                     
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1]})

        return response    