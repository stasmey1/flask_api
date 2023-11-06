from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


class Base(DeclarativeBase):
    ...


db = SQLAlchemy(model_class=Base)
db.init_app(app)


api = Api(app)


