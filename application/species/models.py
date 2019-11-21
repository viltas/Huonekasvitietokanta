from application import db
from application.models import Base

class Species(Base):

    __tablename__ = "species"

    
    genus = db.Column(db.String(144), nullable=False)
    epithet = db.Column(db.String(144), nullable=False)
    water = db.Column(db.Integer, nullable=False)
    light = db.Column(db.Integer, nullable=False)

    ##plants = db.relationship("Plant", backref='species', lazy=True)


    def __init__(self, genus, epithet, name, water, light):
        self.genus = genus
        self.epithet = epithet
        self.name = name
        self.water = water
        self.light = light


    def get_id(self):
        return self.id    