from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class conta(db.Model):
	__tablename__ = "conta"
	id = db.Column(db.Integer, primary_key = True)
	nombre = db.Column(db.String, primary_key = False)
	email = db.Column(db.String, primary_key = False)
	telefono = db.Column(db.Integer, primary_key = False)
	dudas = db.Column(db.String, primary_key = False)

class planes(db.Model):
	__tablename__ = "planes"
	id_plan = db.Column(db.Integer, primary_key = True)
	nombre_cli = db.Column(db.String, primary_key = False)
	email_cli = db.Column(db.String, primary_key = False)
	fono_cli = db.Column(db.Integer, primary_key = False)
	plan = db.Column(db.String, primary_key = False)
