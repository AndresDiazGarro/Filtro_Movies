import pickle
import textwrap

import numpy as np
import streamlit as st

st.header("Sistema de recomendación de peliculas basado en filtro colavorativo")
modelo = pickle.load(open(r'C:/Users/kebelth/Documents/Filtro_Movies/activos/model.pkl', 'rb'))
nombres_peliculas = pickle.load(open(r'C:/Users/kebelth/Documents/Filtro_Movies/activos/peliculas_Nombre.pkl', 'rb'))
clasificaciones_finales = pickle.load(open(r'C:/Users/kebelth/Documents/Filtro_Movies/activos/clasificaciones_Finales.pkl', 'rb'))
peliculas_pivot = pickle.load(open(r'C:/Users/kebelth/Documents/Filtro_Movies/activos/peliculas_Tabla_Pivot.pkl', 'rb'))

#Función para obtener la portada de la pelicula

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


#Función para recomendar pelicula de acuerdo al número de indice del nombre dado como parámetro

def recomendar_Pelicula(nombre_Pelicula):
    lista_peliculas = []
    pelicula_id = np.where(peliculas_pivot.index == nombre_Pelicula)[0][0]
    distancias, indices_sugerencias = modelo.kneighbors(peliculas_pivot.iloc[pelicula_id,:].values.reshape(1,-1), n_neighbors=5)

    for i in indices_sugerencias[0]:
        pelicula_sugerida = peliculas_pivot.index[i]
        lista_peliculas.append(pelicula_sugerida)

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
        st.text(textwrap.fill(libros_recomendados[0], width=10))
        #st.image(url_portada[0])
        
    with col2:
        st.text(textwrap.fill(libros_recomendados[1], width=10))
        #st.image(url_portada[1])
        
    with col3:
        st.text(textwrap.fill(libros_recomendados[2], width=10))  
        #st.image(url_portada[2])
        
    with col4:
        st.text(textwrap.fill(libros_recomendados[3], width=10))
        #st.image(url_portada[3])
        
    with col5:
       st.text(textwrap.fill(libros_recomendados[4], width=10))
        #st.image(url_portada[4])