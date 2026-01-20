import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

API_KEY = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"

pregunta = st.text_input("Escribe tu duda del curso aquí:")

if st.button("Consultar"):
    if pregunta:
        # Fíjate que estas líneas tienen 8 espacios al principio
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{"text": f"Eres un experto en normativa de drones en España. Responde a: {pregunta}"}]
            }]
        }
        
        with st.spinner("Conectando con la IA..."):
            try:
                res = requests.post(url, json=payload, headers=headers)
                if res.status_code == 200:
                    respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(respuesta)
                else:
                    st.error(f"Error {res.status_code}. Prueba a preguntar de nuevo.")
            except Exception as e:
                st.error("Error de conexión.")
    else:
        st.warning("Por favor, escribe una pregunta.")
