import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import plotly as px

st.title('Incidentes reportados de 2018 a 2020 en San Francisco')

data = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")

st.markdown('Base de datos')

df = pd.DataFrame()
df['lat'] = data['Latitude']
df['lon'] = data['Longitude']
df['Dia de la semana'] = data['Incident Day of Week']
df['Año'] = data['Incident Year']
df['Fecha'] = data['Incident Date']
df['Vecindario'] = data['Analysis Neighborhood']
df['Categoria'] = data['Incident Category']
df['Distrito'] = data['Police District']
df['Solucion'] = data['Resolution']
df = df.dropna()
df=df[df['Año']==2020]

df1 = df
neighborhood = st.sidebar.multiselect(
'Vecindario',
df.groupby('Vecindario').count().reset_index()['Vecindario'].tolist())
if len(neighborhood) > 0:
    df1 = df[df['Vecindario'].isin(neighborhood)]

filtrado = df1
district = st.sidebar.multiselect(
'Distrito',
df1.groupby('Distrito').count().reset_index()['Distrito'].tolist())
if len(district) > 0:
    filtrado = df1[df1['Distrito'].isin(district)]
    
filtrado

incidentes = float(len(filtrado)/3)
col1,col2 = st.columns([3,2])   
with col1:
    st.markdown('Ubicación de incidentes')
    st.map(filtrado)
    
with col2:
    st.metric(label='Promedio de incidentes por año', value = incidentes)
    
col3,col4 = st.columns([4,3])

with col3:
    st.markdown('Linea de tiempo de incidentes')
    st.line_chart(filtrado['Fecha'].value_counts())
with col4:
    st.markdown('Día de la semana que se cometieron los crímenes')
    st.bar_chart(filtrado['Dia de la semana'].value_counts())

st.markdown('Tipo de crímenes')
st.bar_chart(filtrado['Categoria'].value_counts())
st.markdown('Estatus de los incidentes')
st.bar_chart(filtrado['Solucion'].value_counts())