from application import db

class Plant(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    date_added = db.Column(db.DateTime, default=db.func.current_timestamp())
    

    name = db.Column(db.String(144), nullable=False)
    pest = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.pest = False