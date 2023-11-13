import pickle
import streamlit as st
import numpy as np

st.header("Sistema de recomendación de peliculas basado en filtro colavorativo")
modelo = pickle.load(open('activos/model.pkl', 'rb'))
nombres_peliculas = pickle.load(open('activos/peliculas_Nombre.pkl', 'rb'))
clasificaciones_finales = pickle.load(open('activos/clasificaciones_Finales.pkl', 'rb'))
peliculas_pivot = pickle.load(open('activos/peliculas_Tabla_Pivot.pkl', 'rb'))

#Función para obtener la portada de la pelicula
"""
def conseguir_portada(sugerencia):
    nombre_pelicula = []
    id_indice = []
    url_portada = []
    
    for pelicula_id in sugerencia:
        nombre_pelicula.append(peliculas_pivot.index[pelicula_id])
        
    for nombre in nombre_pelicula[0]:
        ids = np.where(clasificaciones_finales['Título'] == nombre)[0][0]
        id_indice.append(ids)
        
    for i in id_indice:
        url = clasificaciones_finales.iloc[i]['Url_imagen']
        url_portada.append(url)
        
    return url_portada
"""
#Función para recomendar pelicula de acuerdo al número de indice del nombre dado como parámetro

def recomendar_Pelicula(nombre_Pelicula):
    lista_peliculas = []
    pelicula_id = np.where(peliculas_pivot.index == nombre_Pelicula)[0][0]
    sugerencia = modelo.kneighbors(peliculas_pivot.iloc[pelicula_id,:].values.reshape(1,-1), n_neighbors=5)

    #url_portada = conseguir_portada(sugerencia)

    for i in range(len(sugerencia)):
        peliculas = peliculas_pivot.index[sugerencia[i]]
        for j in peliculas:
            lista_peliculas.append(j)
    return lista_peliculas, #url_portada

# Drop-down con nombres de peliculas

peliculas_seleccionadas = st.selectbox(
    "Ingrese o seleccione una pelicula",
    nombres_peliculas
)

if st.button('Mostrar Recomendaciones'):
    libros_recomendados, = recomendar_Pelicula(peliculas_seleccionadas)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(libros_recomendados[1])
        #st.image(url_portada[1])
        
    with col2:
        st.text(libros_recomendados[2])
        #st.image(url_portada[2])
        
    with col3:
        st.text(libros_recomendados[3])
        #st.image(url_portada[3])
        
    with col4:
        st.text(libros_recomendados[4])
        #st.image(url_portada[4])
        
    with col5:
        st.text(libros_recomendados[5])
        #st.image(url_portada[5])
