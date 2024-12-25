import streamlit as st

st.title("❗ COMPORTAMIENTO DE COLUMNAS ❗")

#############
# CONTAINER 1
#############

# 🔸 declaracion de container
container_1 = st.container(border=True) 
# 🔸 asignar número de columnas
container_1.c1, container_1.c2, container_1.c3 = st.columns(3) 

container_1.title('🔶 Titulo principal dentro del container 1')
container_1.header('🔸 Titulo secundario dentro del container 1')
container_1.subheader('🔸🔸 Subtitulo dentro del container 1')
container_1.c1.button('Columna 1 en Container 1')
container_1.c2.button('Columna 2 en Container 1')
container_1.c3.button('Columna 3 en Container 1')


# 🔸 Botones que no están en ningún contenedor
st.write('Botones que no están dentro de ningún contenedor')
c1, c2 = st.columns(2)
c1.button('Columna 1 sin container')
c2.button('Columna 2 sin container')


############################
# CONTAINER 2 PARA SECCIÓN 2
############################

container_2 = st.container()
container_2.c1, container_2.c2 = st.columns(2)

container_2.title('Sección 2')
container_2.c1.button('Columna 1 en Container 2')
container_2.c2.button('Columna 2 en container 2')


############################
# CONTAINER 3 PARA SECCIÓN 3
############################

container_3 = st.container()
container_3.c1, container_3.c2, container_3.c3 = st.columns(3)

container_3.title('Seccion 3')
container_3.c1.button('Columna 1 en Container 3')
container_3.c2.button('Columna 2 en Container 3')
container_3.c3.button('Columna 3 en Container 3')
