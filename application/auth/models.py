from application import db
from application.models import Base


from sqlalchemy.sql import text


class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    


    plants = db.relationship("Plant", backref='account', lazy=True)


    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        

  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    
    def userrole(self):
        if self.id == 1:
            return ["ADMIN"]
        else:
            return []
    

    @classmethod
    def get_session():
        return session




    