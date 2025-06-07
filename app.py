
import streamlit as st
import requests

# URL de tu backend FastAPI desplegado en Render
URL_BACKEND = "https://lexmaticpro.onrender.com"

# Configuración de la página
st.set_page_config(page_title="LexMatic Pro IA", page_icon="⚖️", layout="centered")

st.title("LexMatic Pro IA")
st.subheader("Abogado Virtual - Buscador de Modelos Jurídicos")

# Menú de categorías
categorias = ["Salud", "Familia", "Laboral", "Discapacidad", "Civil"]
categoria_seleccionada = st.selectbox("Seleccione la categoría jurídica:", categorias)

# Botón para buscar modelos
if st.button("Buscar modelos"):
    try:
        response = requests.get(f"{URL_BACKEND}/buscar", params={"categoria": categoria_seleccionada})
        response.raise_for_status()
        modelos = response.json()
        
        for modelo in modelos:
            st.markdown(f"### {modelo['titulo']}")
            st.markdown(f"**Fundamento:** {modelo['fundamento']}")
            st.markdown(f"{modelo['descripcion']}\n")
            st.markdown("---")
    except Exception as e:
        st.error(f"Error al conectar con el servidor: {e}")
