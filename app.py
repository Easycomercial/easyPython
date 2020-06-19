from flask import Flask, render_template,url_for,request

from modelo import *
from flask_mail import Mail, Message


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://local_user:1234@localhost/CONTACTO"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
def main():
	db.create_all()

mail_settings = {
	"MAIL_SERVER":'smtp.gmail.com',
	"MAIL_PORT":587,
	"MAIL_USE_TLS":True,
	"MAIL_USE_SSl":False,
	"MAIL_USERNAME":'estebansanchezga@gmail.com',
	"MAIL_PASSWORD":'contraseñafalsa'
	}

app.config.update(mail_settings)
mail = Mail(app)
db.init_app(app)

@app.route("/")
def index():
	conta.query.all()
	planes.query.all()
	return render_template("index.html", conta=conta)

@app.route("/plan", methods=['POST'])
def plan():
	db.create_all()
	name_cli= request.form.get("nomcli")
	email_cli= request.form.get("emailcli")
	cell_cli= request.form.get("telefonocli")
	plan= request.form.get("plan")
	addplan = planes(nombre_cli = name_cli, email_cli = email_cli, fono_cli = cell_cli, plan = plan)
	db.session.add(addplan)
	db.session.commit()
	with app.app_context():
		msg = Message(
			subject="Mensaje de prueba",
			sender=app.config.get("MAIL_USERNAME"),
			recipients=['estebandidoedm@gmail.com'],
			html="<header><img src='/img/Logosystem.png'></header><p>Hola, mi nombre es " + name_cli + "\ncon email : " + email_cli + "\nteléfono: " + cell_cli + "\n Y quiero cotizar el plan de:\n " + plan+"\n</p>"
			)
		mail.send(msg)
	return render_template("index.html", message="insertado con exito")

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
	with app.app_context():
		msg = Message(
			subject="Mensaje de prueba",
			sender=app.config.get("MAIL_USERNAME"),
			recipients=['estebandidoedm@gmail.com'],
			body="Hola, mi nombre es " + name + "\ncon email : " + email + "\nteléfono: " + cell + "\n Y tengo la siguiente duda:\n " + desc+"\n"
			)
		mail.send(msg)
	return render_template("index.html", message="insertado con exito")

if __name__ == "__main__":

		app.run()
