from flask import Flask, render_template,url_for,request

from modelo import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://local_user:1234@localhost/CONTACTO"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
	conta.query.all()
	return render_template("index.html", conta=conta)

@app.route("/forma", methods=['POST'])
def forma():
	name= request.form.get("nombre")
	email= request.form.get("email")
	cell= request.form.get("telefono")
	desc= request.form.get("dudas")
	addcon = conta(nombre = name, email = email, telefono = cell, dudas = desc)
	db.session.add(addcon)
	db.session.commit()


if __name__ == "__main__":

		app.run()

