import streamlit as st 
p= st.slider('Choose your principal amount', 100000, 200000)
n= st.slider('Enter the number of years', 1,10)
r= st.slider('Enter the rate of interest', 5.0, 15.0)
emi= p*(r/100)*((1+r/100)**n)/((1+r/100)**n-1)
st.write(emi)