import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

# Tu llave nueva que me pasaste
API_KEY = "AIzaSyADAU-W1wXg8YH9dS_QiNMQd0CzQqTfCA0"

pregunta = st.text_input("Escribe tu duda:")

if st.button("Consultar al experto"):
    if pregunta:
        # CAMBIO: Usamos 'gemini-pro' que es la dirección más fiable
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": pregunta}]
            }]
        }
        
        with st.spinner("Conectando..."):
            try:
                res = requests.post(url, json=payload)
                if res.status_code == 200:
                    respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                    st.success("¡Por fin!")
                    st.write(respuesta)
                else:
                    # Si esto falla, veremos el mensaje real de Google
                    st.error(f"Error {res.status_code}")
                    st.write(res.text)
            except:
                st.error("Error de conexión.")
