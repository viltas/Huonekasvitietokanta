from application import db
from application.models import Base
from sqlalchemy.sql import text
from flask_login import current_user


class Species(Base):

    # create table for species if not already created

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


# find all species that are in users' collections

    @staticmethod
    def find_current_species():
        stmt = text("SELECT Species.id, Species.name  FROM Species"
                    " INNER JOIN Plant ON Plant.species_id = Species.id"
                    " GROUP BY Species.id;")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response
