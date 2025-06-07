
import streamlit as st
import requests
URL_BACKEND = "https://lexmaticpro.onrender.com"

URL_DE_FONDO = "https://lexmaticpro.onrender.com"


st.set_page_config(page_title="LexMatic Pro IA", page_icon="⚖️")

st.title("LexMatic Pro IA")
st.subheader("Abogado Virtual - Buscador de Modelos Jurídicos")

categorias = ["Salud", "Familia", "Laboral", "Discapacidad", "Civil"]
categoria_seleccionada = st.selectbox("Seleccione la categoría jurídica:", categorias)

if st.button("Buscar modelos"):
    try:
        respuesta = requests.get(f"{URL_BACKEND}/buscar", params={"categoria": categoria_seleccionada})
        if respuesta.status_code == 200:
            modelos = respuesta.json().get("resultados", [])
            if modelos:
                for modelo in modelos:
                    with st.expander(modelo['titulo']):
                        st.write(f"**Fundamento:** {modelo['fundamento']}")
                        st.write(modelo['contenido'])
            else:
                st.warning("No se encontraron modelos para esta categoría.")
        else:
            st.error("Error en la respuesta del servidor.")
    except Exception as e:
        st.error(f"Error al conectar con el servidor: {e}")
