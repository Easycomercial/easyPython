from flask import Flask, render_template,url_for,request

from modelo import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://local_user:1234@localhost/CONTACTO"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

	conta.query.all()
	db.session.commit()
	


if __name__ == "__main__":
	with app.app_context():
		main()
