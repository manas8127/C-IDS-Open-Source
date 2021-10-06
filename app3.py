import streamlit as st
import datetime
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
import boto3

sns.set_style('darkgrid')

# ml_model_path = r'C:\Users\lenovo\Documents\Cyber-MADS\pull-three\Cyber_MADS\model_joblib'
# ml_model = joblib.load(os.path.expanduser(ml_model_path))

NEW_AWS_ACCESS_KEY_ID = "AKIAWUZ42VJKZJRRTH2M"
NEW_AWS_SECRET_ACCESS_KEY = "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"

bucket_name = 'cyber-mads-2'

client = boto3.client(
    "s3",
    aws_access_key_id = NEW_AWS_ACCESS_KEY_ID,
    aws_secret_access_key = NEW_AWS_SECRET_ACCESS_KEY,
    region_name = 'ap-south-1'
)

s3 = boto3.resource(
    's3',
    aws_access_key_id = NEW_AWS_ACCESS_KEY_ID,
    aws_secret_access_key = NEW_AWS_SECRET_ACCESS_KEY,
    region_name = 'ap-south-1'
)


def app():
    st.title('Timeline')
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    start_date = st.date_input('Start date', today)
    end_date = st.date_input('End date', tomorrow)
    if start_date < end_date:
        st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
    else:
        st.error('Error: End date must fall after start date.')
    
    df = pd.read_csv('x_test_amex_real.csv')
    dfy = pd.read_csv('y_test_amex_real.csv')

    fig = go.Figure()

    

    date1 = '2017-07-03'
    date2 = '2017-07-07'
    mydates = pd.date_range(date1, date2).tolist()
    mydates = pd.to_datetime(mydates)
    #mydates = mydates.to_numpy()
    #new_array = np.array(mydates.to_pydatetime(), pd.astype('datetime64[D]'))
    
    mydates= mydates.to_period('D')
    df["Time"] = np.random.choice(mydates, size=len(df))
    print(mydates)
    print(type(mydates))
    print((df["Time"].head()))


    

    fig=plt.figure()

    sns.countplot(x=dfy["Label"], hue = df["Time"])
    st.pyplot(fig)

    filename = st.text_input('Enter the file name with extension to download')
    download_location = 'C:/Users/lenovo/Downloads/{}'.format(filename)
    if st.button("Download"):
        client.download_file('cyber-mads-2', filename, download_location)
        st.success("File must have been downloaded!")

    #fig.add_trace(go.Bar(y=dfy['Label'], x=df["Time"],
    #                         name='Bar Chart'))

    


    #st.plotly_chart(fig, use_container_width=True)



    