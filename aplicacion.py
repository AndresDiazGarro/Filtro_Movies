import pickle
import textwrap

import numpy as np
import requests
import streamlit as st

st.header("Sistema de recomendación de peliculas basado en filtro colavorativo")
modelo = pickle.load(open(r'C:/Users/kebelth/Documents/Filtro_Movies/activos/model.pkl', 'rb'))
nombres_peliculas = pickle.load(open(r'C:/Users/kebelth/Documents/Filtro_Movies/activos/peliculas_Nombre.pkl', 'rb'))
clasificaciones_finales = pickle.load(open(r'C:/Users/kebelth/Documents/Filtro_Movies/activos/clasificaciones_Finales.pkl', 'rb'))
peliculas_pivot = pickle.load(open(r'C:/Users/kebelth/Documents/Filtro_Movies/activos/peliculas_Tabla_Pivot.pkl', 'rb'))


#Función para obtener la portada de la pelicula


def obtener_url_imagen(api_key, nombre_pelicula):

    base_url = "https://api.themoviedb.org/3"

    endpoint_busqueda = "/search/movie"


    params = {
        'api_key': api_key,
        'query': nombre_pelicula
    }


    response = requests.get(f"{base_url}{endpoint_busqueda}", params=params)

    if response.status_code == 200:
      
        resultados = response.json()['results']

      
        if resultados and 'poster_path' in resultados[0]:
          
            imagen_path = resultados[0]['poster_path']
            imagen_url = f"https://image.tmdb.org/t/p/w500{imagen_path}"
            return imagen_url
        else:
            return "https://static.vecteezy.com/system/resources/previews/011/860/696/original/its-movie-time-free-vector.jpg"
    


clave_de_api = '095ed49a40a37f91383ca3dfdb74618c'







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
    peliculas_recomendadas, = recomendar_Pelicula(peliculas_seleccionadas)
    col1, col2, col3, col4, col5 = st.columns(5)
           
    with col1:
        st.text(textwrap.fill(peliculas_recomendadas[0], width=10))
        nombre_pelicula_a_buscar = peliculas_recomendadas[0]
        indice_parentesis_apertura = nombre_pelicula_a_buscar.find('(')
        nombre_pelicula_sin_año = nombre_pelicula_a_buscar[:indice_parentesis_apertura].strip()
        url_imagen = obtener_url_imagen(clave_de_api, nombre_pelicula_sin_año)
        st.image(url_imagen)
        
        
    with col2:
        st.text(textwrap.fill(peliculas_recomendadas[1], width=10))
        nombre_pelicula_a_buscar = peliculas_recomendadas[1]
        indice_parentesis_apertura = nombre_pelicula_a_buscar.find('(')
        nombre_pelicula_sin_año = nombre_pelicula_a_buscar[:indice_parentesis_apertura].strip()
        url_imagen = obtener_url_imagen(clave_de_api, nombre_pelicula_sin_año)
        st.image(url_imagen)
        
        
    with col3:
        st.text(textwrap.fill(peliculas_recomendadas[2], width=10))  
        nombre_pelicula_a_buscar = peliculas_recomendadas[2]
        indice_parentesis_apertura = nombre_pelicula_a_buscar.find('(')
        nombre_pelicula_sin_año = nombre_pelicula_a_buscar[:indice_parentesis_apertura].strip()
        url_imagen = obtener_url_imagen(clave_de_api, nombre_pelicula_sin_año)
        st.image(url_imagen)
        
        
    with col4:
        st.text(textwrap.fill(peliculas_recomendadas[3], width=10))
        nombre_pelicula_a_buscar = peliculas_recomendadas[3]
        indice_parentesis_apertura = nombre_pelicula_a_buscar.find('(')
        nombre_pelicula_sin_año = nombre_pelicula_a_buscar[:indice_parentesis_apertura].strip()
        url_imagen = obtener_url_imagen(clave_de_api, nombre_pelicula_sin_año)
        st.image(url_imagen)
        
        
    with col5:
        st.text(textwrap.fill(peliculas_recomendadas[4], width=10))
        nombre_pelicula_a_buscar = peliculas_recomendadas[4]
        indice_parentesis_apertura = nombre_pelicula_a_buscar.find('(')
        nombre_pelicula_sin_año = nombre_pelicula_a_buscar[:indice_parentesis_apertura].strip()
        url_imagen = obtener_url_imagen(clave_de_api, nombre_pelicula_sin_año)
        st.image(url_imagen)
        
  