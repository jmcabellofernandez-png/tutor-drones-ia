import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

# USA TU LLAVE LIMPIA AQUÍ
API_KEY = "TU_LLAVE_AQUÍ"

pregunta = st.text_input("¿Qué quieres saber sobre drones?")

if st.button("Consultar"):
    if pregunta:
        # CAMBIO CLAVE: Usamos v1 y el nombre de modelo sin 'models/'
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": pregunta}]
            }]
        }
        
        try:
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                st.markdown("---")
                st.write(respuesta)
            else:
                # Si falla, nos dirá el error exacto de Google
                st.error(f"Error {res.status_code}")
                st.json(res.json()) 
        except Exception as e:
            st.error(f"Error de conexión: {e}")
