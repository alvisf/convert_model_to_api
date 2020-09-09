from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '#$%23weer5^2@@!009'

    from .upload import upload as upload_blueprint
    from .retrieve import predict as predict_blueprint
    app.register_blueprint(upload_blueprint)
    app.register_blueprint(predict_blueprint)
    return app