import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

pregunta = st.text_input("Escribe tu duda del curso aquí:")

if st.button("Consultar"):
    if pregunta:
        api_key = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": f"Eres un experto en drones en España. Ayuda al usuario con esta duda: {pregunta}"}]}]}
        
        with st.spinner("Pensando..."):
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                st.markdown(respuesta)
            else:
                st.error("Error de conexión con la IA")
