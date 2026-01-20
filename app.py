import streamlit as st
import requests

st.title("🛸 Mi Tutor de Drones")

API_KEY = AIzaSyBJYYLZMgBqtOFFszCRL6oxwowjo1FJ5w0
pregunta = st.text_input("Duda sobre drones:")

if st.button("Consultar"):
    if pregunta:
        # Probamos la versión V1 (la más básica de todas)
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"
        
        payload = {"contents": [{"parts": [{"text": pregunta}]}]}
        headers = {'Content-Type': 'application/json'}
        
        res = requests.post(url, json=payload, headers=headers)
        
        if res.status_code == 200:
            st.write(res.json()['candidates'][0]['content']['parts'][0]['text'])
        else:
            st.error(f"Error {res.status_code}")
            st.write("Google sigue diciendo que el modelo no existe. Por favor, mira el paso de abajo.")
