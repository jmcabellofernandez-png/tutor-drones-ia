import streamlit as st
import requests

st.set_page_config(page_title="Tutor de Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

# 1. Recuperar la llave desde los Secrets
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("⚠️ Falta la llave en los Secrets.")
    st.stop()

pregunta = st.text_input("¿Qué quieres saber sobre drones?")

if st.button("Consultar"):
    if pregunta:
        # CAMBIO AQUÍ: Probamos la ruta 'v1beta' que es la que suele aceptar el modelo flash
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": pregunta}]
            }]
        }
        
        with st.spinner("Consultando..."):
            try:
                res = requests.post(url, json=payload)
                
                if res.status_code == 200:
                    respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                    st.success("Respuesta:")
                    st.write(respuesta)
                else:
                    # Esto nos dirá si sigue siendo 404 u otro error
                    st.error(f"Error {res.status_code}")
                    st.json(res.json())
            except Exception as e:
                st.error(f"Error de conexión: {e}")
