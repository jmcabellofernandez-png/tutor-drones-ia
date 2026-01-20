import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

# Tu llave actual
API_KEY = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"

pregunta = st.text_input("Haz tu pregunta sobre drones:")

if st.button("Consultar"):
    if pregunta:
        with st.spinner("Solicitando acceso a Google..."):
            # Usamos v1 (estable) y gemini-1.0-pro (el que menos falla con el 403)
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.0-pro:generateContent?key={API_KEY}"
            
            headers = {'Content-Type': 'application/json'}
            payload = {
                "contents": [{"parts": [{"text": f"Eres experto en drones. Responde: {pregunta}"}]}]
            }
            
            try:
                res = requests.post(url, json=payload, headers=headers)
                if res.status_code == 200:
                    st.write(res.json()['candidates'][0]['content']['parts'][0]['text'])
                else:
                    st.error(f"Error {res.status_code}. Google no permite el acceso con esta llave.")
                    st.info("Esto significa que necesitamos generar una llave nueva en Google AI Studio.")
            except Exception as e:
                st.error(f"Error: {e}")
