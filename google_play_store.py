import numpy as np 
import pandas as pd 
import plotly.express as px 
import streamlit as st 

data=pd.read_csv('googleplaystore.csv') 
st.write('Author:@AhmedEssam')

st.title('GooglePlayStore')

st.dataframe(data.head())

col1 ,col2 = st.columns(2)

with col1 :
    fig1=px.pie(data, values='Rating' , names='Category',width=500, height=400 ,hole=.3)
    st.plotly_chart(fig1)


with col2:
    fig2=px.pie(data, values='Rating' , names='Content Rating',width=500, 
       color_discrete_sequence=px.colors.sequential.RdBu,height=400 ,hole=.3)
    st.plotly_chart(fig2)    


with col1:
    fig3=px.scatter(data,x='Category', y='Rating',size='Size',
           color='Price',width=500, height=400)
    st.plotly_chart(fig3)


with col2:
    fig4=px.scatter(data,x='Content Rating', y='Price',size='Size',
           color='Type',width=500, height=400)
    st.plotly_chart(fig4)


with col1:
    fig5=px.scatter(data,x='Rating', y='Price',size='Size',
           color='Installs',width=500, height=400)
    st.plotly_chart(fig5) 



with col2:
    fig6=px.bar(data , x='version_y_n', y='Price',width=500, height=400)
    st.plotly_chart(fig6)