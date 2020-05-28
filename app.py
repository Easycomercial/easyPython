from flask import Flask, render_template, url_for , request
from flask_sqlalchemy import SQLAlchemy
from classes.contacto import *
import datetime
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://local_user:1234@localhost/Contacto'
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
db.init_app(app)
def main():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/#contacto", methods=["POST"])
def contacto():
    if request.method() == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        description = request.form.get("description")
        date_entry = datetime.datetime.now()
        contact = Contacto(name=name,email=email,phone=phone,description=description,date_entry=date_entry)
        db.session.add(contact)
        db.session.commit()
        return index()
   


if __name__ == "__main__":
    with app.app_context():
        main()
    app.run()
