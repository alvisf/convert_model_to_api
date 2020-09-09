import pickle
from pymongo import MongoClient
from sklearn import datasets
from sklearn.model_selection import train_test_split

cluster = MongoClient('mongodb+srv://yaganarun:ptnPyqNteCRMXW3e@mlops.wdiah.mongodb.net/ML?authSource=admin&replicaSet=atlas-6k2zs2-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true')
database = cluster.ML
models_collection = database.models
model_name = 'iris model'
model = pickle.loads(models_collection.find_one({'name': model_name})['model'])

iris = datasets.load_iris()
feature = iris.data
target  = iris.target

to_pred = feature[0]
tar = target[0]
predicted = model.predict([to_pred])

print(predicted)