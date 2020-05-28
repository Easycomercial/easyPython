from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contacto(db.Model):
    __tablename__ = "Contacto"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(250), nullable = False)
    date_entry = db.Column(db.DateTime, nullable = False)
    date_delete = db.Column(db.DateTime, nullable = True)

    
        