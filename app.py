#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.metrics import accuracy_score
from flask import Flask, request, jsonify, render_template
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import confusion_matrix
from flask_cors import CORS, cross_origin


# In[2]:


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = pickle.load(open('diagnosis.pkl', 'rb'))
y = pickle.load(open('y_df.pkl', 'rb'))
X = pickle.load(open('X_df.pkl', 'rb'))


# In[ ]:


@app.route('/')
@cross_origin()
def home():
    
        return '<h1> API server is working </h1>'
    
@app.route('/predict', methods = ['GET'])
@cross_origin()
def predict():
    list = ['(vertigo) Paroymsal  Positional Vertigo', 'AIDS' ,'Acne', 'Alcoholic hepatitis' ,'Allergy', 
            'Arthritis', 'Bronchial Asthma','Cervical spondylosis', 'Chicken pox' ,'Chronic cholestasis' ,
            'Dengue','Diabetes' ,'Drug Reaction', 'Fungal infection' ,'GERD', 'Gastroenteritis','Hepatitis B' ,
            'Hepatitis C' ,'Hepatitis D', 'Hepatitis E' ,'Hypertension','Hyperthyroidism' ,'Hypoglycemia' ,
            'Hypothyroidism' ,'Impetigo' ,'Jaundice','Malaria', 'Migraine' ,'Osteoarthristis', 'Paralysis (brain hemorrhage)',
            'Peptic ulcer diseae' ,'Pneumonia', 'Psoriasis', 'Tuberculosis' ,'Typhoid','Urinary tract infection', 'Varicose veins' ,
            'hepatitis A']
    
    parameters = []
    parameters.append(request.args.get('Symptom_1'))
    parameters.append(request.args.get('Symptom_2'))
    parameters.append(request.args.get('Symptom_3'))
    parameters.append(request.args.get('Symptom_4'))
    parameters.append(request.args.get('Symptom_5'))
    parameters.append(request.args.get('Symptom_6'))
    parameters.append(request.args.get('Symptom_7'))
    parameters.append(request.args.get('Symptom_8'))
    parameters.append(request.args.get('Symptom_9'))
    parameters.append(request.args.get('Symptom_10'))
    parameters.append(request.args.get('Symptom_11'))
    
    print(parameters)
    intparameter= []
    for i in range(len(parameters)):
        t = int(parameters[i])
        intparameter.append(t)
        print (intparameter)
    
    
    diagnosis_predict = model.predict([intparameter])
    print ("Your disease has been predicted as: " , diagnosis_predict)
    dis = diagnosis_predict[0]
    
    arry = y.iloc[0:276].values
    arry = arry.ravel()
    idx = []
    j = 0
    for i in range(arry.size):
        if arry[i] == dis:
            idx.append(i)
            j += 1
    X_testing = X.loc[int(idx[0]):int(idx[j-1])]
    X_input = intparameter
    acc_list=[]
    i = 0
    i = int(i)

    while i < j:

        matrix = confusion_matrix(X_testing.iloc[i], X_input)
        matrix
    
        diag = matrix.diagonal()
        rav = matrix.ravel()
        tot_mat = rav.sum()
        tot_diag = diag.sum()

        accuracy = tot_diag/tot_mat
        accuracy
        acc_list.append(accuracy)
        i += 1
    acc_list
    
    acc_list_int = acc_list
    i = 0
    i = int(i)
    while i < j:
        acc_list_int[i] = int(acc_list_int[i] * 100)
        i += 1
    acc_list_int
    
    Accuracy = max(acc_list_int)
    if Accuracy == 100:
        Accuracy = Accuracy - 0.1
        Accuracy = str(Accuracy)
        diseasep = diagnosis_predict[0]
        diseasepredict=list[diseasep]
        return str( diseasepredict+ " " +Accuracy + " % accururacy. Your symptoms are compatible please make an appointment.")
    if Accuracy == 0: 
        Accuracy = str(Accuracy)
        diseasep = diagnosis_predict[0]
        diseasepredict=list[diseasep]        
        return str( diseasepredict+ " " +Accuracy +" % accururacy. Your symptoms were irrelevant beyond compare and we cannot offer you a disease prediction with these inputs." )
    else :
        Accuracy = str(Accuracy)
        diseasep = diagnosis_predict[0]
        diseasepredict=list[diseasep]
        return str( diseasepredict +" " + Accuracy + "% accururacy. Probably due to your irrelevant symptom inputs, you had a low accuracy.\nWe recommend you to try again with more logical symptoms or contact your MD physically.")
        

if __name__ == '__main__':
    app.run(debug=True)

