#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from flask import Flask
from flask import request,jsonify, render_template
import pickle
app = Flask(__name__)


model = pickle.load(open('diagnosis_model2.pkl', 'rb'))
@app.route('/')
def home():
    
        return '<h1> API server is working </h1>'
    

@app.route('/predict')
def predict():
    
    diagnosis_predict= model.predict([[request.args['Symptom_1'],
                                       request.args['Symptom_2'],
                                       request.args['Symptom_3'],
                                       request.args['Symptom_4'],
                                       request.args['Symptom_5'],
                                       request.args['Symptom_6'],
                                       request.args['Symptom_7'],
                                       request.args['Symptom_8'],
                                       request.args['Symptom_9'],
                                       request.args['Symptom_10'],
                                       request.args['Symptom_11']]]) 
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
    


# In[ ]:




