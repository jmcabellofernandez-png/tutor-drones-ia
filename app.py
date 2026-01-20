import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

API_KEY = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"

pregunta = st.text_input("Escribe tu duda sobre drones aquí:")

if st.button("Consultar"):
    if pregunta:
        # Probamos con el modelo más moderno y estable
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{
                "parts": [{"text": f"Eres un experto en normativa de drones en España (EASA y AESA). Responde de forma clara a: {pregunta}"}]
            }]
        }
        
        with st.spinner("Consultando al experto..."):
            try:
                res = requests.post(url, json=payload, headers=headers)
                
                # Si falla el primero (404), intentamos con el modelo Pro automáticamente
                if res.status_code == 404:
                    url_alt = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
                    res = requests.post(url_alt, json=payload, headers=headers)

                if res.status_code == 200:
                    respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                    st.markdown("---")
                    st.markdown(respuesta)
                else:
                    st.error(f"Error {res.status_code}: La IA está ocupada. Inténtalo en un momento.")
            except:
                st.error("Error de conexión. Revisa tu internet.")
    else:
        st.warning("Por favor, escribe una pregunta primero.")
