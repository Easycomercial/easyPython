import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://local_user:1234@localhost/CONTACTO")
db = scoped_session(sessionmaker(bind=engine))

def main():
	conta = db.execute("SELECT id, nombre, email, telefono, dudas FROM conta").fetchall() 
	for contable in conta:
		print(f"{contable.id} , {contable.nombre} , {contable.email}")

if __name__ == "__main__":

	main()

