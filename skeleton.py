import pandas as pd
import streamlit as st
st.write("# Project Name : Campus Placement Machine Learning Model")
st.write("***Model type:*** Classification ")
st.write("***Library Used:*** Pandas , Numpy , Matplotlib , Seaborn , Sklearn , Steamlit")
st.write("## Dataset Used to train:")
data = pd.read_csv("sample_dataset.csv")

st.write(data.sample(10))
st.write("## Student Count: ")
st.bar_chart(data['degree_type'])