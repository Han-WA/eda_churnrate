import streamlit as st
import pandas as pd


def app():
    st.title("Conclusion and Recommendation")

    st.subheader("Key Findings")

    key_finding = {
        "Tenure" : ["-> 27.9 percent of the total customer base has a tenure of 0 to 10 years making the largest customers segment.", 
                          "-> Customers between 0 to 10 tenure years are showing a highest churn rate of over 900 customers (half) out of 1869 compared to others in different tenure ranges.",
                          ]
    }
    
    st.table(pd.DataFrame(key_finding))

    gender = {
        "Gender" : ["-> Regardless of the gender, customers with month-to-month contract are biggest segment in terms of chrun rate."]
    }
    
    st.table(pd.DataFrame(gender))

    contract = {
        "Contract & MultipleLines" : ["-> Month-to-Month contract customer has a significant churn rate with 1655 out of 3872 customers while the total churn is 1869.", 
                      "-> Among month-to-month customers, those with multiple lines service tend to churn the most, followed by customers who don't use phone services."]
    }
    
    st.table(pd.DataFrame(contract))

    partner = {
        "Partner & Dependents" : ["-> Customers without partners and dependents show the highest churn rate, followed by customers with partners but no dependents."]
    }
    
    st.table(pd.DataFrame(partner))

    st.subheader("Recommendation for Retention Strategy")

    retent = '''Tailor retention strategies that address the specific needs and preferences of month-to-month contract customers, irrespective of gender, such as offering promotions or discounts for longer-term contracts. Among month-to-month customers, pay attention to those with multiple lines service, as they tend to churn the most. Consider introducing targeted promotions or improvements in multiple lines services to enhance customer satisfaction and loyalty.'''
    justified_text = f"<div style='text-align: justify;'>{retent}</div>"
    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("##")

    strate = '''Recognizing that customers without partners and dependents exhibit the highest churn rate, developing retention strategies that focus on providing additional value or services to these customers to enhance their overall satisfaction will be effective. '''
    justified_text = f"<div style='text-align: justify;'>{strate}</div>"
    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("##")

    conclu = '''Implementing customer-centric retention strategies, such as personalized promotions, enhanced service offerings, and improved customer support, can help mitigate churn and foster long-term relationships with your telecom company's customer base.'''
    justified_text = f"<div style='text-align: justify;'>{conclu}</div>"
    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("##")

    

