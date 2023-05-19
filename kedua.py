import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64



st.title('Loan Prediction')
st.image('loan_image.jpg')
st.markdown('Dataset:')
data = pd.read_csv('train_loan.csv')
st.write(data.head())
st.markdown('App Income VS Loan Amount')
st.bar_chart(data[['ApplicantIncome', 'LoanAmount']].head(20))

