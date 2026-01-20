import streamlit as st
import requests

# Configuración básica
st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")
st.write("Pregúntame lo que quieras sobre normativa o vuelo de drones.")

# TU LLAVE YA INSTALADA
API_KEY = "AIzaSyADAU-W1wXg8YH9dS_QiNMQd0CzQqTfCA0"

pregunta = st.text_input("Escribe tu duda:")

if st.button("Consultar al experto"):
    if pregunta:
        # Dirección de Google Gemini
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Eres un experto en drones en España. Responde de forma clara y amable a: {pregunta}"}]
            }]
        }
        
        with st.spinner("Pensando..."):
            try:
                res = requests.post(url, json=payload)
                if res.status_code == 200:
                    respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                    st.markdown("---")
                    st.write(respuesta)
                else:
                    st.error(f"Error de Google: {res.status_code}. Prueba de nuevo en un momento.")
            except:
                st.error("Hubo un problema de conexión.")
    else:
        st.warning("Escribe una pregunta primero.")
