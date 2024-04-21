from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import current_user as jwt_current_user

from .index import index_views

from App.models import User, Routines, RoutineWorkouts
from App.database import db

from App.controllers import(
    jwt_required,
    get_workout,
    get_workout_by_bodyPart,
    get_routine_workout,
    add_routine_workout,
    update_routine_workout,
    remove_routine_workout,
    create_routine,
    rename_routine,
    delete_routine,
    get_routine
)

routine_views = Blueprint('routine_views', __name__, template_folder='../templates')

@routine_views.route('/routine/<int:routine_id>', methods=['GET'])
@routine_views.route('/edit_workout/<int:workout_id>', methods=['POST'])
@jwt_required()
def routine_workouts(routine_id, workout_id = None):
    selected_routine = get_routine(routine_id)
    selected_workouts = selected_routine.workouts

    data = request.form

    workout = update_routine_workout(sets = int(data['sets']), reps = int(data['reps']), rest_time = int(data['rest-time']), id = workout.id)

    return render_template('routine.html', routine=selected_routine, workouts=selected_workouts, workout=workout)

@routine_views.route('/myroutines', methods=['GET'])
@routine_views.route('/myroutines/<id>', methods=['GET'])
@jwt_required()
def view_my_routines(routine_id=None):
    routine = None
    if routine_id:
        routine = get_routine(routine_id)


    return render_template('views.html', user=jwt_current_user)

@routine_views.route('/get_byPart/<category>')
@routine_views.route('/get_workout_in_routine')
@jwt_required()
def  get_workouts_for_routine(routine_id=None, category=""):

    data=request.form
    if category == "chest":
        category_get = get_workout_by_bodyPart(category="chest")
    elif category == "back":
        category_get = get_workout_by_bodyPart(category="back")
    elif category == "cardio":
        category_get = get_workout_by_bodyPart(category="cardio")
    elif category == "arms":
        category_get = get_workout_by_bodyPart(category="arms")
    elif category == "legs":
        category_get = get_workout_by_bodyPart(category="legs")
    else: 
        category_get = get_workout_by_bodyPart(category="all")
    routine = get_routine_workout(routine_id)

    return render_template('views.html', get_routine=routine, category_get=category_get)


@routine_views.route('/add_workout_to_routine', methods = ['POST'])
@jwt_required()
def add_routine_workout():
    data = request.form
    selected_routine = RoutineWorkouts.query.filter_by(id=data['routine_id']).first()

    if selected_routine:
        add_routine_workout(routine_id=selected_routine.id, workout_id=workouts.id)

    else:
        workouts = RoutineWorkouts(id=data['routine_id'], workout_id=data['workout_id'], routine_id=data['routine_id'])
    db.session.add(workouts)
    db.session.commit()
    return redirect ('routine.html')

@routine_views.route('/rename_routine/<int:routine_id>', methods=['POST'])
@jwt_required()
def rename_routine_action(routine_id):
    data = request.form
    new_routine_name = rename_routine(  )

@routine_views.route('/delete_routine/<int:routine_id>', methods=['GET'])
@jwt_required()
def delete_routine_action(routine_id):
    if routine_id:
        delete_routine(routine_id)
        flash('Routine Removed')
        return redirect(request.referrer)

