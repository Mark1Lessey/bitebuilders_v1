from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import JWTManager as jwt_current_user
from App.models import db
from App.controllers import (
    create_user, 
    create_workout,
    create_routine,
    get_user_by_username,
    get_workout,
    add_routine_workout,
    )

from App.models import User
import csv

from flask_jwt_extended import(
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
    current_user,
    set_access_cookies,
    unset_jwt_cookies,
    )

index_views = Blueprint('index_views', __name__, template_folder='../templates')



@index_views.route('/', methods=['GET'])
def index_page():
    initialize_db()
    return render_template('login.html')

@index_views.route('/init', methods=['GET'])
def initialize_db():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')

    with open('exercise.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['bodyPart'] == '':
                row['bodyPart'] = None
            if row['equipment'] == '':
                row['equipment'] = None
            if row['name'] == '':
                row['name'] = None
            if row['instructions/0'] == '':
                row['instructions/0'] = None
            if row['instructions/1'] == '':
                row['instructions/1'] = None

            instructions = row['instructions/0'] + row['instructions/1']
            curr_workout = create_workout(row['name'], row['bodyPart'], row['equipment'], instructions)
    print (curr_workout.name)
    print('database intialized')
    return jsonify(message = "Database initialized")

@index_views.route('/index', methods=['GET'])
@jwt_required()
def home_page():
    return render_template('index.html', user=jwt_current_user)