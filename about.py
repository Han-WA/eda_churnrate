import streamlit as st
import pandas as pd


def app():
    st.title("About Data")

    data_intro = '''Telecom customer churn rate, a critical metric in the telecommunications industry, measures the percentage of customers who discontinue their services within a given period. Understanding churn is paramount for telecom companies, as it facilitates proactive strategies to retain customers, enhance service quality, and optimize business operations, ultimately contributing to sustainable growth and customer satisfaction.'''
    justified_text = f"<div style='text-align: justify;'>{data_intro}</div>"
    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("##")

    data_info = {
        "Feature": ["customerId", "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "Device Protection", "TechSupport", "streamingTV", "streamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges", "Churn"],
        "Description": ["Contain customer ID", "whether the customer female or male", "where the customer is a senior citizen or not (1,0)","Whether the customer has a partner or not (Yes, No)", "Whether the customer has dependents or not (Yes, No)", "Number of months the customer has stayed with the company", "Whether the customer has a phone service or not (Yes, No)", "Whether the customer has multiple lines or not (Yes, No, No phone service)", "Customer's internet service provide (DSL, Fiber optic, No)", "Whether the customer has online security or not (Yes, No, No internet service)", "Whether the customer has online backup or not (Yes, No, No internet service)", "Whether the customer has device protection or not (Yes, No)", "Whether the customer has tech support or not (Yes, No)", "Whether the customer has streaming TV or not (Yes, No)", "Whether the customer has streaming movies or not (Yes, No)", "The contract term of the customer (Month-to-Month, One year, Two year)", "Whether the customer has paperless billing or not (Yes, No)", "The customer's payment method (Electronic check, Mailed check, Bank transfer, Credit card)", "The amount charged to the customer monthly", "The total amount charged to the customer", "Whether the customer churned or not (Yes or No)"],
        "Data Type": ["categorical", "categorical", "numeric, int", "categorical", "categorical", "numeric, int", "categorical", "categorical", "categorical", "categorical", "categorical", "categorical","categorical","categorical","categorical", "categorical", "categorical", "categorical",  "numeric, int","object","categorical"],
    }

    df = pd.DataFrame(data_info)
    st.table(df)

    st.write("The following data contains 7043 records and 21 attributes in total.")
    dataset = pd.read_csv("customerchurn.csv")
    st.dataframe(dataset)

    st.subheader("Data Cleaning")
    st.write("First thing first, we need to check the noisiness of our data and see if it requires any cleaning.")

    st.table(dataset.isnull().sum())
    st.write("As you can see here, we've got 11 records missing in TotalCharges value.")
    st.write("Since there are over 7000 records, we have decided to drop those 11 records and continue to our analysis process. Therefore, the records will remain 7032 rows in total.")

    st.subheader("Analysis Process")
    st.write("In this EDA project, we will perform 3 different anlaysis(Univariate, Bivariate, Multivariate) on relevant attributes and find out the correlation between those data")



