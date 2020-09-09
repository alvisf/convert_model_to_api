from flask import Blueprint,render_template, redirect,request,flash
import pickle
import os
from .model import Model
upload = Blueprint('upload' , __name__)
ALLOWED_EXTENSION = ['pkl']
BASE_DIR = os.path.dirname(__file__)

def extension_of(file):
    if file.split('.', 1)[1] in ALLOWED_EXTENSION:
        return True
    else:
        return False

@upload.route('/')
def upload_form():
    return render_template('upload_form.html')

@upload.route('/save_model', methods=['POST'])
def save_model(): #endpoint to upload the model to MongoDB
    if 'model' not in request.files:
        flash('No file available')
    file = request.files['file']
    file_name = file.filename
    if not extension_of(file_name):
        flash('Please choose a file with .pkl')
    file.save(file_name)
    with open(file_name, 'rb') as file:
        model = pickle.load(file)    
    pickled_model = pickle.dumps(model)

    user_name = request.form['user-name']
    model_name = request.form['model-name']
    Model.create_model(user_name , model_name, pickled_model)
    os.remove(file_name) #remove .pkl file after saving it in MongoDB
    return '<p>http://localhost:5000/api/{}/{}</p>'.format(user_name,model_name)

