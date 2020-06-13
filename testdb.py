from flask import flask, render_template,url_for,request

from modelo import *

app = flask(__name__)
app.config["SQLALCHEMY_DATABAS_URI"] = "mysql+pymysql://local_user:1234@localhost/CONTACTO"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	db.create_all()
	addcon = conta(nombre = "patricio", email = "patricio@hotmail.com", telefono = 77993355, dudas = "dudas prueba")
	db.session.add(addcon)
	conta.query.all()
	db.session.commit()


	if __name__ == '__main__':
		with app.app_context():
		 main()