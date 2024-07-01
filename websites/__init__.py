from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:ajith2810@localhost/supermarket'
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
    app.config['SECRET_KEY']='ajithr'
    db.init_app(app)
    from .views import views
    from.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        db.create_all()