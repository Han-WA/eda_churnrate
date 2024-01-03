import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def app():
    st.title("Bivariate Analysis")

    data_intro = '''Bivariate analysis is the simultaneous examination and interpretation of two variables to understand the relationship or pattern between them.It aims to explore the correlation or interaction with changes in another.'''
    justified_text = f"<div style='text-align: justify;'>{data_intro}</div>"
    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("##")

    st.write("In this EDA, we will use Contract and Churn variables for Univariate Analysis and see the relationship with churn attribute")

    dataset = pd.read_csv(r"D:\dashboard\customerchurn.csv")
    dataset.dropna(subset=["TotalCharges"], inplace = True)

    dataset["Churn"] = dataset["Churn"].map({"Yes": 1, "No": 0})

    bins= [0,10,20,30,40,50,60,70,80]

    dataset['tenureRange'] = pd.cut(dataset["tenure"], bins=bins)
    dataset['tenureRange'].astype(str)

    st.write("First, let's see how many of contract types has how many customers.")
    
    cont_code = """
    dataset["Contract"].value_counts()
    """

    st.code(cont_code, language='python')
    st.write(dataset["Contract"].value_counts())
    st.write("There are 3875 Month-to-Month contract customers, 1685 Two-year contract customers, and 1472 One-year contract customers.")

    st.write("Now we know how many customers are there for each contract types, let's group them by churn rate.")

    conandchurn_code = '''
    groupbycontract = dataset.groupby(["Contract"])["Churn"].sum()
    '''
    st.code(conandchurn_code, language='python')

    st.write(dataset.groupby(["Contract"])["Churn"].sum())

    rela_code = '''
    groupbycontract.plot(kind='bar', color = 'red')
plt.xlabel('Contract')
plt.ylabel('Churn')
plt.title('Relation between Contract and Churn data')
plt.show()
    '''
    st.code(rela_code, language='python')

    groupby_contract = dataset.groupby(["Contract"])["Churn"].sum()

    st.title("Relation between Contract and Churn data")

    fig, ax = plt.subplots()
    groupby_contract.plot(kind='bar', color='red', ax=ax)
    plt.xlabel('Contract')
    plt.ylabel('Churn')
    plt.title('Relation between Contract and Churn data')

    st.pyplot(fig)

    st.write("From this, we now know that Month-to-Month contract customer has a significant churn rate with 1655 out of 3872 customers while the total churn is 1869.")














