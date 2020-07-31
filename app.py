from flask import Flask,request ,url_for
from flask_pymongo import PyMongo
import sqlite3
import random
from sqlite3 import Error
import pickle
from gridfs import GridFS, NoFile
from pymongo import MongoClient


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ML_MODEL"
mongo = PyMongo(app)

@app.route("/")
def upload_page():
    return '''
    <form method="POST" action='/uploads' enctype="multipart/form-data">
    <input type="text" name=userId>
    <input type="file" name=modelFile>
    <input type="text" name=apiId>
    <input type="submit">
    </form>
    '''

@app.route("/uploads", methods=["POST"])
def save_upload():
    mongo.save_file(request.form.get('apiId'), request.files["modelFile"])
    mongo.db.model.insert_one({'userId':request.form.get('userId'),'mlModelName':request.form.get('apiId')})
    return "Done"

@app.route('/file/<apiId>')
def files(apiId):
    return mongo.send_file(apiId)

@app.route('/api/<userId>/<apiId>', methods=['GET'])
def genApi(userId, apiId):
    # modelFile=mongo.db.model.find_one_or_404({'userId':userId})
    # # mlfile = url_for('files',apiId=modelFile['mlModelName'])

    # base="fs"
    # version=-1
    # storage = GridFS(mongo.db, base)
    # db = MongoClient().mygrid
    # fs = GridFS(db)
    # f_id = db.stringfiles.files.find_one({ "filename" : "alvisModel.pkl" })
    # data= fs.get(f_id['filename'])
    # fileobj = storage.get_version(filename=apiId, version=version)


    # # mostly copied from flask/helpers.py, with
    # # modifications for GridFS
    # data = wrap_file(request.environ, fileobj, buffer_size=1024 * 255)

    # # mlfile = mongo.send_file(apiId).fileobj
    model = pickle.load(open(data, 'rb'))
    output = model.predict([[2, 9, 6]])
    return ("data")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
