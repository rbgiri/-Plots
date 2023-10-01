import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff


#altair scatter plot
st.header('1. Altair Scatter plot')
Chart_data = pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
Chart = alt.Chart(Chart_data).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(Chart)

st.header('2. Interactive chart')
st.subheader('2.1 Line Chart')
df = pd.read_csv(r"C:\Users\rbgir\OneDrive\Desktop\streamlit\Car_sales.csv")
car_list = df.columns.tolist()
car_choices = st.multiselect('Choose your car',car_list) 
new_df = df[car_choices]
st.line_chart(new_df)

st.subheader('2.2 Area Chart')
st.area_chart(new_df)

st.header('3. DataVisualisation with Plotly')
st.subheader('3.1 Display the Dataset')
df = pd.read_csv(r"C:\Users\rbgir\Downloads\banknotes.csv")
st.dataframe(df.head())

st.subheader('3.2 Pie chart')
fig = px.pie(df,values = 'Diagonal',names = 'Length')
st.plotly_chart(fig)

st.subheader('3.3 Pie Chart with Multiple Parameters')
fig = px.pie(df,values = 'Diagonal',names = 'Length',opacity = 0.7,color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.header('4. Histogram')
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_data = [x1,x2,x3]
group_labels = ['Group-1','Group-2','Group-3']
fig = ff.create_distplot(hist_data,group_labels,bin_size = [.1,.25,.5])
st.plotly_chart(fig)