import streamlit as st

st.title("Health insurance Premium Predict")

# create rows with column to receive input
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

"""
Index(['age', 'region', 'number_of_dependants', 'bmi_category', 'income_lakhs',
       'insurance_plan', 'genetical_risk', 'total_risk_score', 'gender_Male',
       'smoking_status_Occasional', 'smoking_status_Regular',
       'employment_status_Salaried', 'employment_status_Self-Employed'],
      dtype='object')
"""
categorical_options = {
"gender"  :  ['Male','Female'],
"region"  :  ['Northwest', 'Southeast', 'Northeast' ,'Southwest'],
"marital_status"  :  ['Unmarried' ,'Married'],
"bmi_category"  :  ['Normal', 'Obesity' ,'Overweight' ,'Underweight'],
"smoking_status"  :  ['No Smoking', 'Regular' ,'Occasional'],
"employment_status"  :  ['Salaried', 'Self-Employed' ,'Freelancer'],
"income_level"  :  ['<10L' ,'10L - 25L', '> 40L' ,'25L - 40L'],
"insurance_plan"  :  ['Bronze', 'Silver', 'Gold']
}


with row1[0]:
    age = st.number_input('Age', min_value = 18, max_value = 100)
with row1[1]:
    region = st.selectbox("Region", categorical_options["region"] )
with row1[2]:
    number_of_dependants = st.number_input("No. of Dependents", min_value = 0,max_value = 5)

with row2[0]:
    bmi_category = st.selectbox('BMI Category', categorical_options["bmi_category"])
with row2[1]:
    income_lakhs = st.number_input("Income in Lakhs", min_value = 0, max_value = 100)
with row2[2]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options["insurance_plan"])