
import streamlit as st
import requests

# URL de tu backend FastAPI en Render
URL_DE_FONDO = "https://lexmaticpro.onrender.com"

st.set_page_config(page_title="LexMatic Pro IA", page_icon="⚖️", layout="wide")

st.title("LexMatic Pro IA")
st.subheader("Abogado Virtual - Buscador de Modelos Jurídicos")

# Menú de categorías
categorias = ["Salud", "Familia", "Laboral", "Discapacidad", "Civil"]
categoria_seleccionada = st.selectbox("Seleccione la categoría jurídica:", categorias)

if st.button("Buscar modelos"):
    try:
        respuesta = requests.get(f"{URL_DE_FONDO}/buscar?categoria={categoria_seleccionada.lower()}")
        if respuesta.status_code == 200:
            resultados = respuesta.json()
            for resultado in resultados["resultados"]:
                st.markdown(f"### {resultado['titulo']}")
                st.write(f"**Fundamento:** {resultado['fundamento']}")
                st.write(resultado['contenido'])
                st.markdown("---")
        else:
            st.error("No se encontraron resultados.")
    except Exception as e:
        st.error(f"Error al conectar con el servidor: {e}")
