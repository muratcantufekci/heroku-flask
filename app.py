#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from flask import Flask
from flask import request,jsonify, render_template
import pickle
app = Flask(__name__)


model = pickle.load(open('diagnosismodel.pkl', 'rb'))
@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method=='GET':
        return '<h1> API server is working </h1>'
    

@app.route('/predict')
def predict():
   
    diagnosis_predict = model.predict([[15,35,36,12,34,28,23,17,18,18,15]]) 
    return str(diagnosis_predict)


app.run()
    


# In[ ]:




