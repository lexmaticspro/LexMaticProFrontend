
import streamlit as st
import requests

# URL de tu backend FastAPI en Render
URL_BACKEND = "https://lexmaticpro.onrender.com"

st.set_page_config(page_title="LexMatic Pro IA", layout="centered")

st.title("LexMatic Pro IA")
st.subheader("Abogado Virtual - Buscador de Modelos Jurídicos")

# Menú de categorías
categorias = ["Salud", "Familia"]
categoria_seleccionada = st.selectbox("Seleccione la categoría jurídica:", categorias)

if st.button("Buscar modelos"):
    try:
        respuesta = requests.get(f"{URL_BACKEND}/buscar?categoria={categoria_seleccionada}")
        if respuesta.status_code == 200:
            datos = respuesta.json()
            modelos = datos["modelos"]
            if modelos:
                for modelo in modelos:
                    st.write(f"**{modelo['titulo']}**")
                    st.write(f"*Fundamento:* {modelo['fundamento']}")
                    st.write(f"{modelo['descripcion']}")
                    st.markdown("---")
            else:
                st.warning("No se encontraron modelos para la categoría seleccionada.")
        else:
            st.error("Error al obtener los modelos desde el servidor.")
    except Exception as e:
        st.error(f"Error al conectar con el servidor: {str(e)}")
