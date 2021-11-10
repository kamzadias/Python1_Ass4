from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/python1_ass4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tablecoin(db.Model):
    __tablename__ = 'NEWS'
    id = db.Column(db.Integer, primary_key=True)
    name_of_coin = db.Column( db.VARCHAR(255))
    news = db.Column( db.VARCHAR(1000))


    def __init__(self,id,name_of_coin, news):
        self.id = id
        self.name_of_coin = name_of_coin
        self.news = news