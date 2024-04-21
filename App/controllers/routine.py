from App.models import routines, RoutineWorkouts
from App.database import db

def create_routine(user_id, name, id):
    create_routine = routines(id, name, user_id)
    db.session.add(create_routine)
    db.session.commit()
    return create_routine

def rename_routine(routine_id, routine_name):
    cur_routine = routines.query.get(routine_id)
    if cur_routine:
        cur_routine.name = routine_name
        db.session.add(cur_routine)
        db.session.commit()
        return True
    return None

def add_routine_workout(routine_id, workout_id):
    cur_workout = RoutineWorkouts.query.filter_by(routine_id=routine_id, workout_id=workout_id).first()
    if cur_workout:
        return None
    cur_routine_workout = RoutineWorkouts(routine_id, workout_id, 3, 8, 45)
    db.session.add(cur_routine_workout)
    db.session.commit()
    return cur_routine_workout
    
def get_routine_workout(routine_id):
    cur_workout = RoutineWorkouts.query.get(routine_id)
    if cur_workout:
        return cur_workout  
    return None

def remove_routine_workout(routine_id):
    cur_routine_workout = RoutineWorkouts.query.filter_by(id=routine_id).first()
    if cur_routine_workout:
        db.session.delete(cur_routine_workout)
        db.session.commit()
        return True
    return None

def update_routine_workout(routine_id, sets, reps, rest_time):
    cur_workout = RoutineWorkouts.query.get(routine_id)
    cur_workout.sets = sets
    cur_workout.reps = reps
    cur_workout.rest_time = rest_time
    db.session.add(cur_workout)
    db.session.commit()
    return cur_workout

def get_routine(routine_id):
    cur_routine = routines.query.get(routine_id)
    return cur_routine if cur_routine else None

def delete_routine(routine_id):
    cur_routine = routines.query.filter_by(id=routine_id).first()
    if cur_routine.workouts:
        for workoutS in cur_routine.workouts:
            remove_routine_workout(workoutS.id)
    if cur_routine:
        db.session.delete(cur_routine)
        db.session.commit()
        return True
    return None
