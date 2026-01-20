import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Tutor de Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")
st.markdown("---")

# 1. Recuperar la llave desde los Secrets de Streamlit
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("⚠️ ERROR: No se encuentra la llave 'GOOGLE_API_KEY' en los Secrets de Streamlit.")
    st.info("Ve a Settings > Secrets en Streamlit Cloud y pega: GOOGLE_API_KEY = 'tu_llave'")
    st.stop()

# 2. Interfaz de usuario
pregunta = st.text_input("¿En qué puedo ayudarte hoy con los drones?", placeholder="Ej: ¿Qué necesito para volar en ciudad?")

if st.button("Consultar al experto"):
    if pregunta:
        # Usamos la URL estable v1
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": pregunta}]
            }]
        }
        
        with st.spinner("Buscando en la normativa..."):
            try:
                res = requests.post(url, json=payload)
                
                if res.status_code == 200:
                    data = res.json()
                    # Extraer el texto de la respuesta de Google
                    respuesta_texto = data['candidates'][0]['content']['parts'][0]['text']
                    st.success("Respuesta:")
                    st.markdown(respuesta_texto)
                else:
                    st.error(f"Error de Google (Código {res.status_code})")
                    st.json(res.json())
            except Exception as e:
                st.error(f"Error de conexión: {e}")
    else:
        st.warning("Por favor, escribe una pregunta primero.")

st.sidebar.info("Este tutor utiliza IA para responder dudas sobre drones en España.")
