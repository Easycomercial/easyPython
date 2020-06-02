from flask import Flask, render_template,url_for,request
from flask_mail import Mail, Message

from modelo import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://local_user:1234@localhost/CONTACTO"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
mail_settings = {
	"MAIL_SERVER":'smtp.gmail.com',
	"MAIL_PORT":587,
	"MAIL_USE_TLS":True,
	"MAIL_USE_SSl":False,
	"MAIL_USERNAME":'estebansanchezga@gmail.com',
	"MAIL_PASSWORD":'20109887'
	}

app.config.update(mail_settings)
mail = Mail(app)
db.init_app(app)

@app.route("/")
def index():
	conta.query.all()
	return render_template("index.html", conta=conta)

@app.route("/forma", methods=['POST'])
def forma():
	db.create_all()
	name= request.form.get("nombre")
	email= request.form.get("email")
	cell= request.form.get("telefono")
	desc= request.form.get("dudas")
	addcon = conta(nombre = name, email = email, telefono = cell, dudas = desc)
	db.session.add(addcon)
	db.session.commit()
	return render_template("index.html", message="insertado con exito")
	with app.app_context():
		msg = Message(
			subject="Mensaje de prueba",
			sender=app.config.get("MAIL_USERNAME"),
			recipients=['estebandidoedm@gmail.com'],
			body="Hola, mi nombre es " + name + "\ncon email : " + email + "\nteléfono: " + cell + "\n Y tengo la siguiente duda:\n " + desc+"\n"
			)
		print(msg)
		mail.send(msg)

if __name__ == "__main__":

		app.run()

