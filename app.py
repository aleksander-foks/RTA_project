#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from flask import Flask
from flask import request
from flask import jsonify
import pickle
from perceptron import Perceptron

app = Flask(__name__)

@app.route('/home')
def hello():
    print("Hello World")

@app.route('/api/predict', methods = ["GET"])
def get_prediction():
    sepal_length = float(request.args.get('sl', "1"))
    #print(sepal_length)
    sepal_width = float(request.args.get('sw', "1"))
    petal_length = float(request.args.get('pl', "1"))
    petal_width = float(request.args.get('pw', "1"))
    
    features = [sepal_length, sepal_width, petal_length, petal_width]
    
    with open("perceptron_iris.pkl", "rb") as picklefile:
        model = pickle.load(picklefile)
    print(model)
    
    predicted_class = int(model.predict(features))
    
    return jsonify(features = features, predicted_class = predicted_class)


if __name__ == "__main__":
    app.run(host = "0.0.0.0")

