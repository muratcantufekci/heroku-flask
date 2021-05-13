#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from flask import Flask
from flask import request,jsonify, render_template
import pickle
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = pickle.load(open('diagnosis_model2.pkl', 'rb'))
@app.route('/')
@cross_origin()
def home():
    
        return '<h1> API server is working </h1>'
    

@app.route('/predict')
@cross_origin()
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
    return str(diagnosis_predict)

if __name__ == '__main__':
    app.run(debug=True)
    


# In[2]:





# In[ ]:




