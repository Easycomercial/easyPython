from flask import Flask, render_template,url_for,request

from modelo import *
from flask_mail import Mail, Message
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://local_user:1234@localhost/CONTACTO"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
def main():
	db.create_all()

mail_settings = {
	"MAIL_SERVER": 'smtp.gmail.com',
	"MAIL_PORT": 465,
	"MAIL_USE_TLS": False,
	"MAIL_USE_SSL": True,
	"MAIL_USERNAME": "correopruebapatricio@gmail.com",
	"MAIL_PASSWORD": "patricio1234567"
	}

app.config.update(mail_settings)
mail = Mail(app)

db.init_app(app)

@app.route("/")
def index():
	conta.query.all()
	return render_template("index.html", conta=conta)

@app.route("/formul", methods=['POST'])
def formul():
    name= request.form.get("nombre")
    email= request.form.get("email")
    cell= request.form.get("telefono")
    desc= request.form.get("dudas")
    addcon = conta(nombre = name, email = email, telefono = cell, dudas = desc)
    db.session.add(addcon)
    db.session.commit()
    with app.app_context():
        msg = Message(
            subject="Contacto EasySystems Prueba",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["perezsoto0717@gmail.com"],
            body="hola, mi nombre es " + name + "\ncon email : " + email + "\ntelefono: " + cell + "\ntengo la siguiente duda:\n" + desc + "\n"
            )
        mail.send(msg)
    return render_template("index.html", message="insertado")

@app.route("/planc", methods=['POST'])
def planc():
    name_clie= request.form.get("nombreclie")
    email_clie= request.form.get("emailclie")
    cell_clie= request.form.get("telefonoclie")
    plan_clie= request.form.get("planclie")
    addplan = planes(nombre_cli = name_clie, email_cli = email_clie, fono_cli = cell_clie, plan = plan_clie)
    db.session.add(addplan)
    db.session.commit()
    with app.app_context():
        msg = Message(
            subject="Contacto EasySystems Prueba",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["perezsoto0717@gmail.com"],
            body="hola, mi nombre es " + name_clie + "\ncon email : " + email_clie + "\ntelefono: " + cell_clie + "\n plan elegido:\n" + plan_clie + "\n"
            )
        mail.send(msg)
    return render_template("index.html", message="insertado")
if __name__ == "__main__":

		app.run()
