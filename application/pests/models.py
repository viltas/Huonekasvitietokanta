from application import db
from application.models import Base

class Pest(Base):
    
   
    name = db.Column(db.String(144), nullable=False)
    control = db.Column(db.String(250), nullable=False)
                       

    def __init__(self, name, control):
        self.name = name
        self.control = control


def get_id(self):
        return self.id   