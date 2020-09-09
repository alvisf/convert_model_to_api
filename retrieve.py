from flask import Blueprint, request, render_template
import pickle
import json
from .model import Model
predict = Blueprint('predict' , __name__)

def find_class(pred_class):
    output = ['Setosa' , 'Versicolour' , 'Virginica']
    return output[pred_class]

@predict.route('/api/<user_name>/<apiID>' , methods = ['POST'])
def predict_classifier(user_name , apiID):
    # print(user_name , apiID)
    clf = pickle.loads(Model.get_model(user_name , apiID))
    data = json.loads(request.data)
    inp = [ data[key] for key in data ]
    return find_class(clf.predict([inp])[0] )

@predict.route('/classifier_form')
def predict_form():
    return render_template('predict.html')

