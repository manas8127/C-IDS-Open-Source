import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px


def app():
    st.title('Reports')
    dfx = pd.read_csv('x_test_amex_real.csv')
    dfxi=dfx.iloc[0:1000]
    dfy = pd.read_csv(r'y_test_amex_real.csv')
    dfyi=dfy.iloc[0:1000]
    # df=pd.read_csv(r'C:\Cyber_MADS\testing.csv')
    x_axis = st.selectbox(
        "Choose a column for its relationship with the Label", dfx.columns)
    #y_axis = st.selectbox("Choose a variable for the y-axis", dfy.columns)
    #ax = sns.stripplot(x_axis, dfy.Label)
    #ax.set(xlabel ='', ylabel ='Label')
    # st.write(dfx[x_axis])
    # st.write(dfy['Label'])
    chart_visual = st.selectbox(
        'Select Charts/Plot type', ('Line Chart', 'Bar Chart', 'Bubble Chart'))

    fig = go.Figure()
    
    if chart_visual == 'Line Chart':
        fig.add_trace(go.Scatter(x=dfyi['Label'], y=dfxi[x_axis],
                                 mode='lines', name='Line Chart'))
  

    elif chart_visual == 'Bar Chart':
        fig.add_trace(go.Bar(x=dfyi['Label'], y=dfxi[x_axis],
                             name='Bar Chart'))
   
    elif chart_visual == 'Bubble Chart':
        fig.add_trace(go.Scatter(x=dfyi['Label'], y=dfxi[x_axis],
                                 mode='markers',
                                 marker_size=[40, 60, 80, 60, 40, 50],
                                 name='Bubble Chart'))


    st.plotly_chart(fig, use_container_width=True)

    '''
    fig = px.scatter(
        x=dfy['Label'],
        y=dfx[x_axis],
    )
    fig.update_layout(
        xaxis_title="Label",
        yaxis_title="Work",
    )
    st.write(fig)
    '''