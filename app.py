#import section
from flask import Flask, render_template, url_for , request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail , Message
from classes.contacto import *
import datetime
import os

#Flask app configuration 
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://local_user:1234@localhost/Contacto'
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False


#configuration for gmail 
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "damian.quiroz.68148254916@gmail.com",
    "MAIL_PASSWORD": "68148254916.goroshii"
}

app.config.update(mail_settings)
mail = Mail(app)

#database configuration 
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/#contacto", methods=["POST"])
def contacto():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        description = request.form.get("description")
        date_entry = datetime.datetime.now()
        contact = Contacto(name=name,email=email,phone=phone,description=description,date_entry=date_entry)
        db.session.add(contact)
        db.session.commit()
        with app.app_context():
            msg = Message(subject="Contacto EasySystems prueba",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["damian.quiroz.13@sansano.usm.cl"],
            body="Hola, mi nombre es " + name + "\ncon email : " + email + "\nteléfono: " + phone + "\n Y tengo la siguiente duda:\n " + description+"\n"
            )
            mail.send(msg)
    return index()
   


if __name__ == "__main__":
    app.run()
