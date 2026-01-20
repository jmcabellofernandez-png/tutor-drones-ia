import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

# Tu llave nueva
API_KEY = "AIzaSyADAU-W1wXg8YH9dS_QiNMQd0CzQqTfCA0"

pregunta = st.text_input("Escribe tu duda:")

if st.button("Consultar"):
    if pregunta:
        # Probamos con la dirección 'latest' que es la más compatible
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{"parts": [{"text": pregunta}]}]
        }
        
        with st.spinner("Buscando respuesta..."):
            res = requests.post(url, json=payload)
            
            if res.status_code == 200:
                respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                st.write(respuesta)
            else:
                st.error(f"Error {res.status_code}")
                st.info("Si sale 404 de nuevo, necesitamos activar el modelo en Google AI Studio.")
                st.write(res.text)
