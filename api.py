import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base



engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:root@127.0.0.1:3306/crud")




print(engine.table_names())



Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    nom = sqlalchemy.Column(sqlalchemy.String(length=100))
    email = sqlalchemy.Column(sqlalchemy.String(length=255))



class school(Base):
    __tablename__ = 'school'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=100))
   
    


Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()



newEmployee = user(id=17,nom="khalid44", email="khalid@gmail.com")
school1 = school(id=14,name="M6")
users = Session.query(user).filter_by(nom="mehdi")
print(users.__dict__)


Session.commit()