import pickle

with open ("model.pkl" , 'rb') as f:
    classifier = pickle.load(f)

def predict_outcome(secondary_percent, secondary_branch, highschool_percent,
       high_school_branch, hsc_s, degree_percent, degree_type,
       work_xp, employment_test_percent, specialisation, mba_percent):
    
    prediction = classifier.predict([[secondary_percent, secondary_branch, highschool_percent,
       high_school_branch, hsc_s, degree_percent, degree_type,
       work_xp, employment_test_percent, specialisation, mba_percent]])
    
    print(prediction)
    return prediction

import streamlit as st

st.write('Testing....')
