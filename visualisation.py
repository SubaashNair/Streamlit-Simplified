import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def main1():
    st.title('Diabetes Dataframe')
    df = pd.read_csv('diabetes.csv')
    st.dataframe(df)

    # using pyplot function

    fig = plt.figure()
    df['Outcome'].value_counts().plot(kind='bar')
    plt.title('Outcome Distribution')
    plt.ylabel('Frequency')
    st.pyplot(fig)

    fig1 = plt.figure()
    df['Pregnancies'].value_counts().plot(kind='kde')
    plt.title('Outcome Distribution')
    plt.ylabel('Frequency')
    st.pyplot(fig1)

    fig2 = plt.figure()
    sns.countplot()
    plt.title('Outcome Distribution')
    plt.ylabel('Frequency')
    st.pyplot(fig2)
main1()


def main2():
    st.title('Bank Dataframe')
    df1 = pd.read_csv('bank-full.csv')
    st.dataframe(df1)
    
    fig3 = plt.figure()
    sns.countplot(x= 'default',data=df1)
    plt.title('Loan Default Distribution')
    st.pyplot(fig3)

    fig4 = plt.figure()
    sns.barplot(x='job',y='balance', hue='marital', data=df1)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig4)

    # using streamlit builtin functions
    st.header('Balance vs Job')
    st.bar_chart(df1, y='balance', x='job')

    st.line_chart(df1, x='age', y='balance')


    # using plotly

    fig5 = px.pie(values = df1['balance'], names=df1['marital'], title='Bank Balance and Marriage Status')
    st.plotly_chart(fig5)

    fig6 = px.bar(df1, x='job',y='age')
    st.plotly_chart(fig6)
    
main2()