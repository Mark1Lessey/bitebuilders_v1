from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import current_user as jwt_current_user

from App.models import Workouts

from App.models import db

from App.controllers import ( 
    get_all_workouts,
    get_workout_by_bodyPart
)
workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/view_workout')
def views_workouts():
    workouts = get_all_workouts()
    return render_template('workout_views.html', workouts=workouts)

@workout_views.route('/get_byPart/<category>')
def by_body(category):
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

    return render_template('views.html', category_get=category_get)