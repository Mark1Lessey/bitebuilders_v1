from App.models import routines, routine_workouts
from App.database import db

def create_routine(user, name):
    custom_routine = routines(user, name)
    db.session.add(custom_routine)
    db.session.commit()
    return custom_routine

def rename_workout(self, name):
    cur_routine = routines.query.filter_by(id=self.id).first()
    if cur_routine:
        cur_routine.name = name
        db.session.add(cur_routine)
        db.session.commit()
        return True
    return None

def add_workout(routine_id, workout_id):
    current_workout = routine_workouts.query.filter_by(routine_id=routine_id, workout_id=workout_id).first()
    if current_workout:
        return None
    cur_routine_workout = routine_workouts(routine_id, workout_id, 3, 8, 45)
    db.session.add(cur_routine_workout)
    db.session.commit()
    return cur_routine_workout
    

def remove_workout(id):
    cur_workout = routine_workouts.query.filter_by(id=id).first()
    if cur_workout:
        db.session.delete(cur_workout)
        db.session.commit()
        return True
    return None

def get_routine(id):
    cur_routine = routines.query.get(id)
    return cur_routine if cur_routine else None

def update_routine(id, sets, reps, rest_time):
    cur_workout = routine_workouts.query.get(id)
    cur_workout.sets = sets
    cur_workout.reps = reps
    cur_workout.rest_time = rest_time
    db.session.add(cur_workout)
    db.session.commit()
    return cur_workout

def get_routine_workout(id):
    cur_workout = routine_workouts.query.get(id)
    if cur_workout:
        return cur_workout  
    return None


def delete_routine(id):
    cur_routine = routines.query.filter_by(id=id).first()

    if cur_routine.workouts:
        for r in cur_routine.workouts:
            remove_workout(r.id)
    
    if cur_routine:
        db.session.delete(cur_routine)
        db.session.commit()
        return True
    return None
