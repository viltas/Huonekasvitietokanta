from application import db
from application.models import Base

class Pest(Base):
    
    # create table for pests if not already created
   
    description = db.Column(db.String(400), nullable=False)
    control = db.Column(db.String(400), nullable=False)
                       

    def __init__(self, name, description, control):
        self.description = description
        self.control = control


def get_id(self):
        return self.id   