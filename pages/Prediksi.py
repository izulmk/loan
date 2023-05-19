import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No": 1, "Yes": 2}
    for key, value in feature_dict.items():
        if val == key:
            return value

def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value


st.image('loan_image.jpg')
st.subheader('You need to fill all necessary informations in order to get a reply to your loan request')
st.sidebar.header('Information about the client:')
gender_dict = {'Male': 1, 'Female': 2}
feature_dict = {'No': 1, 'Yes': 2}
edu = {'Graduate': 1, 'Not Graduate': 2}
prop = {'Rural': 1, 'Urban': 2, 'Semiurban': 3}
ApplicantIncome = st.sidebar.slider('ApplicantIncome', 0, 10000, 0)
CoapplicantIncome = st.sidebar.slider('CoapplicantIncome', 0, 10000, 0)
LoanAmount = st.sidebar.slider('LoanAmount in K$', 0, 700)
Loan_Amount_Term = st.sidebar.selectbox('Loan_Amount_Term', (12.0, 36.0, 60.0, 84.0, 120.0, 180.0, 240.0, 300.0, 360.0))
Credit_History = st.sidebar.radio('Credit_History', (0.0, 1.0))
Gender = st.sidebar.radio('Gender', tuple(gender_dict.keys()))
Married = st.sidebar.radio('Married', tuple(feature_dict.keys()))
Self_Employed = st.sidebar.radio('Self_Employed', tuple(feature_dict.keys()))
Dependents = st.sidebar.radio('Dependents', options=['0', '1', '2', '3+'])
Education = st.sidebar.radio('Education', tuple(edu.keys()))
Property_Area = st.sidebar.radio('Property_Area', tuple(prop.keys()))
class_0, class_3, class_1, class_2 = 0, 0, 0, 0

if Dependents == '0':
   class_0 = 1
elif Dependents == '1':
   class_1 = 1
elif Dependents == '2':
   class_2 = 1
else:
   class_3 = 1
Rural = 1  # Assuming this is the default value, modify it according to your requirements
Urban = 2
Semiurban = 3
data1 = {
        'Gender': Gender,
        'Married': Married,
        'Dependents': [class_0, class_1, class_2, class_3],
        'Education': Education,
        'ApplicantIncome': ApplicantIncome,
        'CoapplicantIncome': CoapplicantIncome,
        'Self_Employed': Self_Employed,
        'LoanAmount': LoanAmount,
        'Loan_Amount_Term': Loan_Amount_Term,
        'Credit_History': Credit_History,
        'Property_Area': [Rural, Urban, Semiurban],
    }

feature_list = [
        data1['ApplicantIncome'],
        data1['CoapplicantIncome'],
        data1['LoanAmount'],
        data1['Loan_Amount_Term'],
        data1['Credit_History'],
        get_value(data1['Gender'], gender_dict),
        get_value(data1['Married'], feature_dict),
        data1['Dependents'][0],
        data1['Dependents'][1],
        data1['Dependents'][2],
        data1['Dependents'][3],
        get_value(data1['Education'], edu),
        get_value(data1['Self_Employed'], feature_dict),
        data1['Property_Area'][0],
        data1['Property_Area'][1],
        data1['Property_Area'][2]
    ]

single_sample = np.array(feature_list).reshape(1, -1)
    
if st.button('Click to Predict'):
        file_ = open('6m-rain.gif', 'rb')
        contents = file_.read()
        data_url = base64.b64encode(contents).decode('utf-8')
        file_.close()

        file_ = open('green-cola-no.gif', 'rb')
        contents = file_.read()
        data_url_no = base64.b64encode(contents).decode('utf-8')
        file_.close()

        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0:
            st.error('According to our calculations, you will not get the loan from the bank')
            st.markdown(f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">', unsafe_allow_html=True)
        elif prediction[0] == 1:
            st.success('Congratulations! You will get a loan from the bank')
            st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)
