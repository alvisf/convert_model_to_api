from pymongo import MongoClient
cluster = MongoClient('mongodb+srv://yaganarun:ptnPyqNteCRMXW3e@mlops.wdiah.mongodb.net/ML?authSource=admin&replicaSet=atlas-6k2zs2-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true')
database = cluster.ML
models_collection = database.models


class Model():
    @staticmethod
    def create_model(user_name , model_name, model):
        models_collection.insert_one({'user_name':user_name,'model_name': model_name, 'model': model})
        return 'Created {} model'.format(model_name)

    @staticmethod
    def get_model(user_name , model_name):
        return models_collection.find_one({'user_name':user_name,'model_name': model_name})['model']
