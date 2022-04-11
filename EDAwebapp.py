# Import Libraries

import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# WEbAPp  title

st.markdown('''
# **Exploratory Data Analysis web application**
This app is developed by Zartashia_ codanics student named **EDA app**
''')

# Allowing file upload in app
with st.sidebar.header("Upload your dataset in (.csv)"):
    uploaded_file= st.sidebar.file_uploader("upload your file", type=["csv"])
    # you  can also add a data example to display for user help
    df= sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009/download))")
    
    # Profiling report for Pandas 

if uploaded_file is not None:
    @st.cache    # to increase dataset upload speed
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr= ProfileReport(df, explorative=True)
    st.header('**Input DF')
    st.write(df)
    st.write("---")
    st.header('**Profiling report with Pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for Csv file to upload')
    if st.button('Presss to use example data'):
        # example dataset
        def load_data():
            a= pd.DataFrame(np.random.rand(100,5),
                            columns=['age','banana','codanics', 'code', 'ear'])
            return a
        df=load_data()
        pr= ProfileReport(df, explorative=True)
        st.header('**Input DF**')
        st.write(df)
        st.write("---")
        st.header('**Profiling report with Pandas**')
        st_profile_report(pr)