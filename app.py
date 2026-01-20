import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

# Usamos la llave que ya sabemos que conecta
API_KEY = "AIzaSyBJYYLZMgBqtOFFszCRL6oxwowjo1FJ5w0"

pregunta = st.text_input("Escribe tu duda sobre drones:")

if st.button("Consultar"):
    if pregunta:
        # La URL correcta para evitar el 400
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        # Estructura de datos exacta que pide Google
        payload = {
            "contents": [
                {
                    "parts": [{"text": pregunta}]
                }
            ]
        }
        
        headers = {'Content-Type': 'application/json'}
        
        with st.spinner("Obteniendo respuesta..."):
            try:
                res = requests.post(url, json=payload, headers=headers)
                
                if res.status_code == 200:
                    # Extraemos la respuesta del laberinto de datos de Google
                    data = res.json()
                    respuesta = data['candidates'][0]['content']['parts'][0]['text']
                    st.success("Respuesta del experto:")
                    st.write(respuesta)
                else:
                    st.error(f"Error {res.status_code}")
                    st.write(res.text) # Esto nos dirá qué palabra exacta no le gusta
            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Por favor, escribe algo.")
