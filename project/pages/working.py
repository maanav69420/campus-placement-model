import pickle
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import pandas as pd

pickle_in = open("C:/Users/maanav aditya/OneDrive/Documents/GitHub/campus-placement-model/model.pkl", "rb")
classifier = pickle.load(pickle_in)
def predict_outcome(secondary_percent, secondary_branch, highschool_percent,
       high_school_branch, hsc_s, degree_percent, degree_type,
       work_xp, employment_test_percent, specialisation, mba_percent):
    
    input_val = np.array([[secondary_percent ,secondary_branch, highschool_percent,high_school_branch,hsc_s,degree_percent,degree_type ,specialisation,
          mba_percent,work_xp,employment_test_percent]])
    
    prediction = classifier.predict(input_val)
    
    print(prediction)
    return prediction

import streamlit as st

st.write('Testing....')


secondary_branch_val = ['Others' ,'Central']
high_school_branch_val = ['Others', 'Central']
hsc_s_val = ['Commerce', 'Science' ,'Arts']
degree_type_val = ['Sci&Tech' ,'Comm&Mgmt' ,'Others']
work_xp_val = ['No' , 'Yes']
specialisation_val = ['Mkt&HR' , 'Mkt&Fin']


def main():
    st.title('Campus placement recrutment Classifier')
    html_temp = """
<div style = "background-color: cyan ; padding: 10px">
<h2 style="color: white; text-align: center">Steamlit Classifier</h2>
"""

    st.markdown(html_temp , unsafe_allow_html = True)
    secondary_percent = st.text_input("mention the percentage u received in secondary school:") 

    secondary_branch = st.radio("pick the branch you chose in secondary school:" , options = secondary_branch_val)

    highschool_percent =st.text_input("percentage scored in highschool:")

    high_school_branch = st.radio("mention the branch you chose in highschool :" , options =high_school_branch_val)

    hsc_s = st.radio("pick the subject you chose in high school:" , hsc_s_val)

    degree_percent = st.text_input("mention the percentage you recieved in college :")

    degree_type = st.radio("pick the subject for degree:" , options = degree_type_val)

    work_xp = st.radio("Do you have any work experience:" , options =work_xp_val)

    employment_test_percent = st.text_input("mention your percentage in employment test")

    specialisation = st.radio("mention your specialization:" , options =specialisation_val)

    mba_percent = st.text_input("mention your mba percentage :")
    
    result = ''
    if st.button('predict'):
        result = predict_outcome(secondary_percent, secondary_branch, highschool_percent,
       high_school_branch, hsc_s, degree_percent, degree_type,
       work_xp, employment_test_percent, specialisation, mba_percent)
    st.success('the outcome is {}'.format(result))

if __name__ == '__main__':
    main()