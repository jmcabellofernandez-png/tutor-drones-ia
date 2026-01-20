import streamlit as st
import requests

st.title("🛸 Mi Tutor de Drones")

# Aquí ya no pegamos la llave, la lee de forma segura desde los Secrets
try:
    API_KEY = st.secrets["AIzaSyA8mzDtkfR72AtTfKjT3kkTBBajeSKp1e8"]
except:
    st.error("⚠️ Falta la llave en los Secrets de Streamlit.")
    st.stop()

pregunta = st.text_input("Haz tu consulta:")

if st.button("Consultar"):
    if pregunta:
        # Usamos la versión estable v1
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        payload = {"contents": [{"parts": [{"text": pregunta}]}]}
        
        res = requests.post(url, json=payload)
        
        if res.status_code == 200:
            st.write(res.json()['candidates'][0]['content']['parts'][0]['text'])
        else:
            st.error(f"Error {res.status_code}")
            st.json(res.json())
