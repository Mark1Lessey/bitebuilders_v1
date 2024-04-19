from App.database import db

class RoutineWorkouts(db.Model):
	__tablename__ = "routine_workouts"
	id = db.Column(db.Integer, primary_key=True)
	routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'), nullable =False)
	workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable = False)
	workout = db.relationship('Workouts')
	sets = db.Column(db.Integer, nullable = False )
	reps = db.Column(db.Integer, nullable = False)
	restTime = db.Column(db.Integer, nullable = False)
	

	def __init__(self, routine_id, workout_id, sets, reps, restTime):
		self.sets = sets
		self.reps = reps
		self.restTime = restTime
		self.routine_id = routine_id
		self.workout_id = workout_id


