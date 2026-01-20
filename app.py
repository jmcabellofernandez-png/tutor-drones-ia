import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

# Usamos la llave que ya probamos en Colab
API_KEY = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"

pregunta = st.text_input("Escribe tu duda del curso aquí:")

if st.button("Consultar"):
    if pregunta:
        # Usamos el modelo 1.5-flash que es el más estable
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}
        
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{"text": f"Eres un experto en normativa de drones en España. Responde de forma clara y educativa a: {pregunta}"}]
            }]
        }
        
        with st.spinner("Conectando con el experto..."):
            try:
                res = requests.post(url, json=payload, headers=headers)
                if res.status_code == 200:
                    datos = res.json()
                    respuesta = datos['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(respuesta)
                else:
                    st.error(f"Error de la IA (Código {res.status_code}): {res.text}")
            except Exception as e:
                st.error(f"Error de conexión: {e}")
    else:
        st.warning("Por favor, escribe una pregunta.")
