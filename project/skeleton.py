import pandas as pd
import streamlit as st
st.write("# Project Name : Campus Placement Machine Learning Model")
st.write("***Model type:*** Classification ")
st.write("***Library Used:*** Pandas , Numpy , Matplotlib , Seaborn , Sklearn , Steamlit")
st.write("## Dataset Used to train:")
data = pd.read_csv("C:/Users/maanav aditya/OneDrive/Documents/GitHub/campus-placement-model/sample_dataset.csv")
data = data.drop(['Unnamed: 0'] , axis = 1)
st.write(data.sample(10))
st.write("## Student Count: ")


st.bar_chart(data = data , x = 'secondary_branch', y  ='secondary_percent')