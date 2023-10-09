from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
import os


# create the extension
db = SQLAlchemy()


def create_app():
    # create the app
    app = Flask(__name__, template_folder='../templates/')

    # set secret key for flask session
    app.secret_key = os.urandom(24)

    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    # initialize the app with the extension
    db.init_app(app)


    from . import views

    app.register_blueprint(views.core)


    return app




