from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import current_user as jwt_current_user

from .index import index_views

from App.models import User

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

@routine_views.route('/get_workout_in_routine/<int:routine_id>')
def  get_workouts_for_routine(routine_id):
    routine = get_routine(routine_id)
    workouts = routine.workouts

    workout_data = [{'workout': {'name': workout.workout.name}, 'sets': workout.sets, 'reps': workout.reps, 'rest_time': workout.rest_time} for workout in workouts]

    return jsonify({'workouts': workout_data})

@routine_views.route('/add_workout_to_routine/<int:routine_id>', methods = ['POST'])
@jwt_required()
def add_routine_workout(routine_id, category='all'):
    data = None
    exercises = get_workout_by_bodyPart(category)
    selected_routine = get_routine(routine_id)
    workouts = selected_routine.workouts

    if request.method == 'POST':
        data = request.form
        exercise_id = data.getlist('exercise-id')
        for id in exercise_id:
            add_routine_workout(routine_id=routine_id, workout_id=id)

        return redirect(url_for('routines_views.routine_workouts', id = routine_id, routine_workout_id = None))
    return render_template('routine_adder.html', routine = selected_routine, workouts = workouts, exercises = exercises)

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

@routine_views.route('/ceate_routine/<category>', methods=['GET'])
@routine_views.route('/create_routine', methods = ['POST'])
@jwt_required()
def create_routine_action(category = 'all'):
    workouts = get_workout_by_bodyPart(category)

    if request.method == 'POST':
        data = request.form
        routine = create_routine(jwt_current_user, data['routine_name'])
        exercise_id = data.getlist('excercise_id')
        for id in exercise_id:
            add_routine_workout(routine_id = routine.id, workout_id = id)

        return redirect(url_for('routine_views.view_routine_action'))
    return render_template('createroutine.html', workouts=workouts)
