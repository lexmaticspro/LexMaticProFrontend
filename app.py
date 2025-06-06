import streamlit as st
import requests

# URL de tu backend FastAPI en Render
BACKEND_URL = "https://lexmaticpro.onrender.com"

st.set_page_config(page_title="LexMatic Pro IA", page_icon="⚖️", layout="centered")

st.title("LexMatic Pro IA")
st.subheader("Abogado Virtual - Buscador de Modelos Jurídicos")

# Menú de categorías
categorias = ["Salud", "Familia", "Laboral", "Discapacidad", "Civil"]
categoria_seleccionada = st.selectbox("Seleccione la categoría jurídica:", categorias)

# Botón de búsqueda
if st.button("Buscar modelos"):

    url = f"{BACKEND_URL}/buscar?categoria={categoria_seleccionada}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        if "resultados" in datos:
            for modelo in datos["resultados"]:
                st.markdown(f"### {modelo['titulo']}")
                st.write(f"**Contenido:** {modelo['contenido']}")
                st.write(f"**Fundamento:** {modelo['fundamento']}")
                st.write("---")

        elif "resultados_aproximados" in datos:
            st.warning("No hubo coincidencias exactas. Resultados aproximados:")
            for modelo in datos["resultados_aproximados"]:
                st.markdown(f"### {modelo['titulo']}")
                st.write(f"**Contenido:** {modelo['contenido']}")
                st.write(f"**Fundamento:** {modelo['fundamento']}")
                st.write("---")
        else:
            st.error("No se encontraron modelos para esta categoría.")
    else:
        st.error("Error al conectar con el servidor.")
