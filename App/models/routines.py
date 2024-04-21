from App.database import db

class Routines(db.Model):
	__tablename__ = "routines"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	workouts = db.relationship('RoutineWorkouts', backref='routines')

	def __init__(self, id, user_id, name):
		self.id=id
		self.name = name
		self.user_id = user_id

	def get_json(self):
		return{
			'id': self.id,
			'user': self.user.firstName,
			'Routine name': self.name
		}

