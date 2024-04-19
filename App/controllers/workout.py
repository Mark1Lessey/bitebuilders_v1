from App.models import Workouts
from App.database import db

def create_workout(name, bodyPart, equipment, instructions):
    createWorkout = Workouts(name, bodyPart, equipment, instructions)
    db.session.add(createWorkout)
    db.session.commit()
    return createWorkout