import streamlit as st
import pickle

st.title("Iris plant prediction")
sl=st.number_input("Enter sepal length")
sw=st.number_input("Enter sepal width")
pl=st.number_input("Enter petal length")
pw=st.number_input("Enter pepal width")
button=st.button("Predict")

if button:
    model=pickle.load(open("iris.pkl","rb"))
    res=model.predict([[sl,sw,pl,pw]])[0]
    st.markdown(f"Predicted Iris Class: {res}")
