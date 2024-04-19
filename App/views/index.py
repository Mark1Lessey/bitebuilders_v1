from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import JWTManager as jwt_current_user
from App.models import db
from App.controllers import create_user, createWorkout

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
    current_user,
    )

index_views = Blueprint('index_views', __name__, template_folder='../templates')

def initialize_db():
    db.drop_all()
    db.create_all()
    user = create_user('')

    with open('exercises.csv') as csvfile:
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
        createWorkout(row['name'], row['bodyPart'], row['equipment'], instructions)


    print('database intialized')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')
'''
@index_views.route('/index', methods=['GET'])
@jwt_required()
def home_page():
    return 
'''
@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})