from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class conta(db.Model):
	__tablename__ = "conta"
	id = db.Column(db.Integer,nullable=False, primary_key= True)
	nombre = db.Column(db.String,nullable=False, primary_key= False)
	email = db.Column(db.String,nullable=False, primary_key= False)
	telefono = db.Column(db.Integer,nullable=False, primary_key= False)
	dudas= db.Column(db.String,nullable=False, primary_key= False)

