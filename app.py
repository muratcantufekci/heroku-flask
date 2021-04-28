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
    msg_data={}
    for k in request.args.keys():
        val=request.args.get(k)
        msg_data[k]=val
    f = open("models/X_test.json","r")
    X_test = json.load(f)
    f.close()
    all_cols=X_test
    input_df=pd.DataFrame(msg_data,columns=all_cols,index=[0])
    arr_results = model.predict(input_df)
    treatment_likelihood=""
    return treatment_likelihood
   
   # diagnosis_predict= model.predict([[request.args['Symptom_1'],
    #                                   request.args['Symptom_2'],
     #                                  request.args['Symptom_3'],
      #                                 request.args['Symptom_4'],
       #                                request.args['Symptom_5'],
        #                               request.args['Symptom_6'],
         #                              request.args['Symptom_7'],
          #                             request.args['Symptom_8'],
           #                            request.args['Symptom_9'],
            #                           request.args['Symptom_10'],
             #                          request.args['Symptom_11']]]) 
    #return str(diagnosis_predict)

if __name__ == '__main__':
    app.run(debug=True)
    


# In[ ]:




