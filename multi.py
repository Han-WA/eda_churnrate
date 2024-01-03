import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


def app():
    st.title("Multivariate Analysis")

    st.write("Multivariate analysis involves the simultaneous examination and interpretation of three or more variables within a dataset. It aims to provide a comprehensive understanding of how multiple factors interact and influence each other.")

    dataset = pd.read_csv("customerchurn.csv")
    dataset.dropna(subset=["TotalCharges"], inplace = True)

    dataset["Churn"] = dataset["Churn"].map({"Yes": 1, "No": 0})

    bins= [0,10,20,30,40,50,60,70,80]

    dataset['tenureRange'] = pd.cut(dataset["tenure"], bins=bins)
    dataset['tenureRange'].astype(str)

    churn_code = """
    churnTable = pd.pivot_table(dataset, index=["gender"], columns=["Contract"], values=["Churn"], aggfunc=np.sum)
    """

    st.code(churn_code, language='python')

    churnTable = pd.pivot_table(dataset, index=["gender"], columns=["Contract"], values=["Churn"], aggfunc=np.sum)
    st.dataframe(churnTable)

    code = """
    churnPlot = px.histogram(dataset, x='gender', y= 'Churn', color='Contract',barmode='group', title="Relationship between Customers Churn Rate, gender and their contract types")
    """

    st.code(code, language='python')

    churnPlot = px.histogram(dataset, x='gender', y= 'Churn', color='Contract',barmode='group', title="Relationship between Customers Churn Rate, gender and their contract types")
    st.plotly_chart(churnPlot)

    st.write("Interestingly, among month-to-month customers, a little over half are female, and the remaining half are male.")

    st.subheader("Analysis on Multiple Lines Service, Contract and Churn Rate")

    inter_code = """
    internet_contract = pd.pivot_table(data=dataset,index='MultipleLines',columns='Contract',values='Churn',aggfunc='mean')"""
    
    st.code(inter_code, language='python')

    internet_contract = pd.pivot_table(data=dataset,index='MultipleLines',columns='Contract',values='Churn',aggfunc='mean')
    
    st.dataframe(internet_contract)

    plt.figure(figsize=[8, 5])
    sns.heatmap(internet_contract, annot=True, cmap='RdYlGn')
    st.subheader("Multiple Line and Contract Heatmap")
    st.pyplot(plt)

    st.write("Looking at the heatmap, it's clear that among month-to-month customers, those with multiple lines tend to churn the most, followed by customers who don't use phone services")

    st.subheader("Analysis on Partner, Dependents and Churn Rate")

    partner_dependent = pd.pivot_table(data=dataset, index="Partner", columns='Dependents', values="Churn")

    plt.figure(figsize=[6, 3])
    sns.heatmap(partner_dependent, annot=True, cmap='Reds')
    st.pyplot(plt)
    st.write("According to the heatmap, customers without partner and dependents tend to have significant churn rate followed by customers with Partner but no dependents while customers with both partner and dependents are the lowest in churn rate.")


















