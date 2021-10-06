import streamlit as st
import joblib
import os
import pandas as pd
import boto3
import seaborn as sns

sns.set_style('darkgrid')


def ml_model():
    mj=joblib.load('model_joblib')
    df = pd.read_csv('x_test_amex_real.csv')
    for i in range(1, 21):
        d=df.iloc[i-1:i]
        st.write("\n")
        st.write("\n")
        st.write(d)
        port = d['Destination Port']
        val = mj.predict(d)
        if val == 0:
            st.success("Benign network, NORMAL TRAFFIC detected!")
        elif val == 1:
            st.error("DDoS attack detected! PORT {} will be closed for the next 10 minutes".format(port.to_string(index=False)))
        elif val == 2: 
            st.error("PortScan attack detected! PORT {} will be closed for the next 10 minutes".format(port.to_string(index=False)))
        elif val == 3:
            st.error("Bot attack detected! PORT {} will be closed for the next 10 minutes".format(port.to_string(index=False)))
        elif val == 4: 
            st.error("Infiltration attack detected! PORT {} will be closed for the next 10 minutes".format(port.to_string(index=False)))
        elif val == 5: 
            st.error("Web attack (Brute Force) detected! PORT {} will be closed for the next 10 minutes".format(port.to_string(index=False)))
        elif val == 6:
            st.error("Web attack (XSS) detected! PORT {} will be closed for the next 10 minutes".format(port.to_string(index=False)))
        elif val == 7:
            st.error("Web attack (SQL Injection) detected! PORT {} will be closed for the next 10 minutes".format(port.to_string(index=False)))
        else:
            st.error("FTP-Patator attack detected! PORT {} will be closed for the next 10 minutes".format(port.to_string(index=False)))


def app():
    st.title('Dashboard')
    ml_model()
    


'''
    sns.countplot(x=df['Destination Port'], data=df, hue=df['Label'])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
'''
