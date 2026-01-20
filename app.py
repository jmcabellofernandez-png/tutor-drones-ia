import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

API_KEY = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"

pregunta = st.text_input("Escribe tu duda del curso aquí:")

if st.button("Consultar"):
    if pregunta:
        # Estas líneas de abajo TIENEN que tener espacios al principio (sangría)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{"text": f"Eres un experto en drones en España. Responde a: {pregunta}"}]
            }]
        }
        
        with st.spinner("Conectando..."):
            res = requests.post(url, json=payload, headers=headers)
            if res.status_code == 200:
                respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                st.markdown(respuesta)
            else:
                st.error(f"Error: {res.status_code}")
