from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from . import settings


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

CORS(
    app,
    resources={
        r"/.*": {
            "origins": ["http://0.0.0.0", "http://localhost", "http://www.jakdf.us"]
        }
    },
)

db = SQLAlchemy(model_class=Base)


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI

# initialize the app with the extension
db.init_app(app)

from app.routers import *  # noqa sorry for this
