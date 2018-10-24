from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Car(db.Model):

	__tablename__ = "car_info"

	car_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	vin = db.Column(db.String(200))
	color = db.Column(db.String(200))
	four_door = db.Column(db.Boolean)
	two_door = db.Column(db.Boolean)
	drivetrain = db.Column(db.String(200))

	def __repr__(self):
		"""provide helpful representation when printed."""
		return "<Car car_id={} vin={} color={} four_door={} two_door={} drivetrain={}>".format(
													self.car_id, self.vin, self.color,
													self.four_door, self.two_door,
													self.drivetrain)

##### #### #### ####
def connect_to_db(app):
	"""Connect the database to our Flask app."""

	#Configure to use our PstgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///carinfo'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
	app.config['SQLALCHEMY_ECHO'] = True 
	db.app = app
	db.init_app(app) 

if __name__ == "__main__":
	from rest_api import app
	connect_to_db(app)
	print("Connected to DB")