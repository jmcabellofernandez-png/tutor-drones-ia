import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

# Tu clave que ya funciona
API_KEY = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"

pregunta = st.text_input("Escribe tu duda sobre el curso de drones:")

if st.button("Consultar"):
    if pregunta:
        # Probamos con la URL más directa y simplificada posible
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Eres un experto en drones en España. Responde brevemente: {pregunta}"}]
            }]
        }
        
        with st.spinner("Conectando con Google..."):
            try:
                res = requests.post(url, json=payload)
                if res.status_code == 200:
                    respuesta = res.json()['candidates'][0]['content']['parts'][0]['text']
                    st.markdown("---")
                    st.info(respuesta)
                else:
                    # Si falla, te mostraré el mensaje real de Google para saber qué hacer
                    st.error(f"Google dice: {res.status_code}")
                    st.write(res.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Escribe una pregunta.")
