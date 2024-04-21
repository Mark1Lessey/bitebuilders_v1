from App.database import db

class RoutineWorkouts(db.Model):
	__tablename__ = "routine_workouts"
	id = db.Column(db.Integer, primary_key=True)
	routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'), nullable =False)
	workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable = False)
	workout = db.relationship('Workouts')
	

	def __init__(self, id, routine_id, workout_id):
		self.id = id
		self.routine_id = routine_id
		self.workout_id = workout_id


