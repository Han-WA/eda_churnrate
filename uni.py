import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("Univariate Analysis")

    data_intro = '''Univariate analysis use single variable in isolation, providing insights into its distribution, central tendency and disperasion. It is fundamental statistical approach used to understand the characeteristics and patterns of individual variables within a dataset'''
    justified_text = f"<div style='text-align: justify;'>{data_intro}</div>"
    st.markdown(justified_text, unsafe_allow_html=True)
    st.markdown("##")

    st.write("In this EDA, we will use tenure variable for Univariate Analysis and see the relationship with churn attribute")

    dataset = pd.read_csv("customerchurn.csv")
    dataset.dropna(subset=["TotalCharges"], inplace = True)
    # Central Tendency
    st.subheader("Central Tendency")

    central_code = """
    print('Average tenure year :', dataset['tenure'].mean())
    print('Median tenure year  :', dataset['tenure'].median())
    print('Mode tenure year    :', dataset['tenure'].mode()) """

    st.code(central_code, language='python')

    st.markdown("Average tenure year : {}".format(dataset['tenure'].mean()))
    st.markdown("Median tenure year  : {}".format(dataset['tenure'].median()))
    st.markdown("Mode tenure year    : {}\n".format(dataset['tenure'].mode()))


    st.subheader("Dispersion(Range, Variance)")
    disper_code = """
    print('Variance of tenure                    :', dataset['tenure'].var())
print('Difference between Max and Min tenure :', dataset['tenure'].max()-dataset['tenure'].min())
print('Standard Deviation of tenure          :', dataset['tenure'].std())
print('Quantile range of tenure              :', dataset['tenure'].quantile([.25,.5,.75])) """

    st.code(disper_code, language='python')

    st.markdown("Variance of tenure         : {}".format(dataset['tenure'].var()))
    st.markdown("Difference between Max and Min tenure : {}".format(dataset['tenure'].max()-dataset['tenure'].min()))
    st.markdown("Variance of tenure         : {}".format(dataset['tenure'].std()))
    st.markdown("Variance of tenure         : {}\n".format(dataset['tenure'].quantile([.25,.5,.75])))

    st.subheader("Data Discretization for Tenure Distribution")

    disti_code = """
    bins= [0,10,20,30,40,50,60,70,80]
tenure = pd.cut(dataset["tenure"], bins=bins).value_counts()

tenure.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Tenure Distribution')
plt.axis('equal')
plt.show()"""

    st.code(disti_code, language='python')

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    tenure = pd.cut(dataset["tenure"], bins=bins).value_counts()
    fig, ax = plt.subplots()
    tenure.plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_title('Tenure Distribution')
    ax.axis('equal')
    st.pyplot(fig)

    st.write("As you can see in the pie chart, 27.9 percent of the total customer base has a tenure of 0 to 10 years making the largest customers segment.")

    st.subheader('Relationship with Churn')

    st.write("First, we need to change the churn data type from categorical to numeric, int(1,0), 1 meaning Yes and 0 for No.")

    churn_code = """
    dataset["Churn"] = dataset["Churn"].map({"Yes": 1, "No": 0})
    dataset["Churn"].value_counts()"""

    st.code(churn_code, language='python')

    dataset["Churn"] = dataset["Churn"].map({"Yes": 1, "No": 0})
    st.write(dataset["Churn"].value_counts())

    st.write("From here, we can know 1869 customers has discontinued the service while 5163 customers are still using the service.")

    bins= [0,10,20,30,40,50,60,70,80]

    dataset['tenureRange'] = pd.cut(dataset["tenure"], bins=bins)
    dataset['tenureRange'].astype(str)

    groupby_tenure = dataset.groupby(["tenureRange"])["Churn"].sum()

    st.subheader("Relation between Tenure and Churn data")

    fig, ax = plt.subplots()
    groupby_tenure.plot(kind='bar', color='blue', ax=ax)
    plt.xlabel('Tenure Range')
    plt.ylabel('Churn')
    plt.title('Relation between Tenure and Churn data')

    st.pyplot(fig)

    st.write("According to this graph, customers between 0 to 10 tenure years are showing a highest churn rate of over 900 customers (half) out of 1869 compared to others in different tenure ranges.")
