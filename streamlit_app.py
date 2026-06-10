import streamlit as st
import os
from google import genai
from google.genai import types
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# --- CONFIGURACIÓN E INICIALIZACIÓN ---
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

@st.cache_resource
def get_client():
    return genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

client = get_client()

# Contexto de Marca Nexara (La ESENCIA del proyecto)
NEXARA_BRAND = """Eres el Asistente Ejecutivo de Nexara Finance (Dir: Luz Dalia Granados). 
Tono: Riguroso, resolutivo, empático. 
Reglas: 
1. Siempre ofrecer la auditoría como valor añadido. 
2. Usar azul corporativo y verde para métricas positivas.
3. Si hablas del Plan A o Plan B, destaca el ahorro inmediato."""

# --- TAB 1: GESTIÓN (CORREO AUTOMATIZADO) ---
def enviar_correo(dest, asunto, cuerpo):
    # Asume token.json presente en la raíz
    creds = Credentials.from_authorized_user_file('token.json')
    service = build('gmail', 'v1', credentials=creds)
    msg = MIMEText(cuerpo)
    msg['to'] = dest
    msg['subject'] = asunto
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    service.users().messages().send(userId='me', body={'raw': raw}).execute()

# --- INTERFAZ DEL SISTEMA ---
st.markdown("# 🚀 Nexara Finance OS")

t1, t2, t3 = st.tabs(["📩 Gestión de Clientes", "📈 Factoría de Marketing", "📅 Planificador Operativo"])

with t1:
    st.subheader("Comunicación Directa con Cliente")
    email = st.text_input("Email Cliente")
    instr = st.text_area("¿Qué queremos lograr?", placeholder="Ej: Convencer para Plan Avanzado tras diagnóstico...")
    if st.button("Automatizar Propuesta"):
        res = client.models.generate_content(model='gemini-1.5-flash', contents=instr,
                config=types.GenerateContentConfig(system_instruction=NEXARA_BRAND))
        st.session_state.draft = res.text
    if 'draft' in st.session_state:
        cuerpo = st.text_area("Borrador:", value=st.session_state.draft, height=200)
        if st.button("Enviar desde Gmail"):
            enviar_correo(email, "Propuesta Nexara Finance", cuerpo)
            st.success("Correo enviado.")

with t2:
    st.subheader("Factoría de Marketing (Crecimiento)")
    canal = st.selectbox("Canal:", ["LinkedIn", "Newsletter", "Video Corto"])
    if st.button("Generar Plan Estratégico"):
        res = client.models.generate_content(model='gemini-1.5-flash', 
                contents=f"Genera 3 posts para {canal} sobre ahorro fiscal.",
                config=types.GenerateContentConfig(system_instruction=NEXARA_BRAND))
        st.markdown(res.text)

with t3:
    st.subheader("Procesamiento de Auditorías")
    notas = st.text_area("Datos crudos de auditoría:")
    if st.button("Procesar Informe de Fugas"):
        res = client.models.generate_content(model='gemini-1.5-flash', 
                contents=f"Analiza estas notas y extrae fugas de dinero para Nexara: {notas}",
                config=types.GenerateContentConfig(system_instruction=NEXARA_BRAND))
        st.info(res.text)
        st.info(resp.text)
