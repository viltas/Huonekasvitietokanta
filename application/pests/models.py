from application import db
from application.models import Base

class Pest(Base):
    
   
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    control = db.Column(db.String(400), nullable=False)
                       

    def __init__(self, name, description, control):
        self.name = name
        self.description = description
        self.control = control


def get_id(self):
        return self.id   