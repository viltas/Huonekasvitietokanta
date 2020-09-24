from application import db
from application.models import Base
from sqlalchemy.sql import func


from sqlalchemy.sql import text


class User(Base):

# create join table for user accounts if not already created

    __tablename__ = "account"
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
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


# find users with no plants
    @staticmethod
    def find_new_users():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Plant ON Plant.account_id = Account.id"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Plant.id) = 0")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response


    @classmethod
    def get_session():
        return session




    