from application import db
from application.models import Base

class Plant(Base):
    pest = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)


    #species_id = db.Column(db.Integer, db.ForeignKey('species.id'),
    #                       nullable=True)

    def __init__(self, name):
        self.name = name
        self.pest = False