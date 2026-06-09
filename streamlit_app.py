import os
import base64
import streamlit as st
from google import genai
from google.genai import types
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 1. CONFIGURACIÓN INICIAL Y SEGURIDAD
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Lectura segura desde los Secrets de Streamlit
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("Error crítico: API Key no configurada en los Secrets.")
    st.stop()

# Inicialización del cliente oficial de Google
try:
    client = genai.Client()
except Exception as e:
    st.error(f"Error al conectar con la IA: {e}")
    st.stop()

# 2. CONTEXTO DE NEGOCIO Y FUNCIONES DE GMAIL (NO TOCAR)
NEXARA_CONTEXT = "Eres el Asistente Ejecutivo Central de Nexara Finance. Directora: Luz Dalia Granados Diaz. Plan A: Avanzado AI-Driven. Plan B: Rescate Financiero."

SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly']

def obtener_servicio_gmail():
    # Tu lógica original de autenticación se mantiene aquí intacta
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    return build('gmail', 'v1', credentials=creds) if creds and creds.valid else None

# 3. DASHBOARD Y UI
st.title("Nexara Finance · Centro de Control AI")

tab1, tab2, tab3 = st.tabs(["📩 Gestión de Correos", "📈 Marketing", "📅 Reuniones"])

with tab1:
    st.subheader("Gestión de Comunicaciones")
    # ... Tu lógica de UI original aquí ...

with tab2:
    st.subheader("Factoría de Marketing")
    canal = st.selectbox("Canal:", ["LinkedIn", "Newsletter", "Video"])
    if st.button("Generar Estrategia"):
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=f"Genera contenido para {canal} con el estilo Nexara.",
            config=types.GenerateContentConfig(system_instruction=NEXARA_CONTEXT)
        )
        st.markdown(response.text)

with tab3:
    st.subheader("Planificación")
    # ... Tu lógica de UI original aquí ...
