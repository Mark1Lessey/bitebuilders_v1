from App.database import db

class Workouts(db.Model):
    __tablename__ = "workouts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bodyPart = db.Column(db.String(100), nullable=False)
    equipment = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.String(500), nullable=False)

    def __init__(self, id, name, bodyPart, equipment, instructions):
        self.id = id
        self.name = name
        self.bodyPart = bodyPart
        self.equipment = equipment
        self.instructions = instructions

