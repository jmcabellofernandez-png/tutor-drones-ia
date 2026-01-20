import streamlit as st
import requests

st.set_page_config(page_title="Tutor Drones", page_icon="🛸")
st.title("🛸 Mi Tutor de Drones")

API_KEY = "AIzaSyAMnsCYE5JvPcWQ0up-goXmALEnbWr2jfQ"

pregunta = st.text_input("Haz tu pregunta sobre drones:")

if st.button("Consultar"):
    if pregunta:
        with st.spinner("Buscando el modelo adecuado en tu cuenta..."):
            try:
                # 1. PASO MAESTRO: Preguntamos qué modelos tienes tú
                list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
                response = requests.get(list_url).json()
                
                # Buscamos en tu lista el primer modelo que permita generar contenido
                model_name = None
                for m in response.get('models', []):
                    if 'generateContent' in m.get('supportedGenerationMethods', []):
                        model_name = m['name']
                        break
                
                if model_name:
                    # 2. Usamos el modelo que Google nos ha dicho que SÍ tienes
                    url = f"https://generativelanguage.googleapis.com/v1beta/{model_name}:generateContent?key={API_KEY}"
                    payload = {"contents": [{"parts": [{"text": f"Eres experto en drones en España. Responde: {pregunta}"}]}]}
                    
                    res = requests.post(url, json=payload)
                    if res.status_code == 200:
                        st.success(f"Conectado vía {model_name}")
                        st.write(res.json()['candidates'][0]['content']['parts'][0]['text'])
                    else:
                        st.error(f"Error al responder: {res.status_code}")
                else:
                    st.error("No se encontró ningún modelo activo en esta API KEY.")
                    
            except Exception as e:
                st.error(f"Error de conexión: {e}")
