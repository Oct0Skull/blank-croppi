import streamlit as st
import numpy as np
import pandas as pd

st.title(':sparkles: PRO DASHBOARD :sparkles:')

###########
# SECCION 1
###########
st.subheader('Sección 1')
t1s1, t2s1, t3s1 = st.tabs(['Grafica 1', 'Grafica 2', 'Grafica 3'])
t1s1.line_chart(data=np.random.randn(10,1))
t2s1.line_chart(data=np.random.randn(10,1))
# t3s1.line_chart(data=np.random.randn(10,1))

t31s1, t32s1 = t3s1.tabs(['Grafica 3.1', 'Grafica 3.2'])
t31s1.bar_chart(data=np.random.randn(10,1))
t32s1.bar_chart(data=np.random.randn(10,1))


###########
# SECCION 2
###########
st.subheader('Sección 2')
c1_2, c2_2 = st.columns(2)

c1_2.write('.')
c1_2.write('.')
c1_2.write('.')
c1_2.bar_chart(data=np.random.randn(10,1), horizontal=True)

map_data = pd.DataFrame(
    np.random.randn(250,2) / [50,50] + [41.37, 2.15],
    columns=['lat', 'lon'])

c2_2.map(map_data, zoom=10)


###########
# SECCION 3
###########
st.subheader('Sección 3')
c1_3, c2_3 = st.columns(2)

c1_3.container(border=True).metric("Temperatura", "27 ºC", "16 ºF")
c2_3.container(border=True).metric("Viento", "9 mph", "-8%")
