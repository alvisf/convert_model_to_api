from flask import Blueprint, request, render_template
import pickle
import json
from .model import Model
predict = Blueprint('predict' , __name__)

def find_class(pred_class):
    output = ['Setosa' , 'Versicolour' , 'Virginica']
    return output[pred_class]

@predict.route('/predict' , methods = ['GET' , 'POST'])
def predict_classifier():
    if request.method == 'POST':
        model_name = 'iris model'
        clf = pickle.loads(Model.get_model(model_name))
        data = json.loads(request.data)
        inp = []
        for key in data:
            inp.append(data[key])
        return find_class(clf.predict([inp])[0] )
    else:
        return render_template('predict.html')
