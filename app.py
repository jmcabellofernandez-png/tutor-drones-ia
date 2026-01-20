import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

API_KEY = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"

pregunta = st.text_input("Escribe tu duda sobre drones aquí:")

if st.button("Consultar"):
    if pregunta:
        # CAMBIO CLAVE: Usamos la versión v1 estable y el modelo flash directo
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{"text": f"Eres un experto en normativa de drones en España. Responde de forma clara a: {pregunta}"}]
            }]
        }
        
        with st.spinner("Consultando..."):
            try:
                res = requests.post(url, json=payload, headers=headers)
                
                if res.status_code == 200:
                    respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                    st.markdown("---")
                    st.write(respuesta)
                else:
                    # Este mensaje nos dirá si el problema es la llave o el modelo
                    st.error(f"Error {res.status_code}: {res.text}")
            except Exception as e:
                st.error(f"Error de conexión: {e}")
    else:
        st.warning("Escribe algo primero.")
