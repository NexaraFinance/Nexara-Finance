import os
import base64
import streamlit as st
from email.mime.text import MIMEText
from google import genai
from google.genai import types

# Integración oficial de la API de Gmail de Google
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 1. CONFIGURACIÓN INICIAL Y SEGURIDAD
st.set_page_config(page_title="Nexara Finance OS - Centro de Control AI", layout="wide")

# Gestión de API Key (Prioriza st.secrets para el funcionamiento 24/7)
GEMINI_API_KEY = st.secrets.get("GOOGLE_API_KEY", "Fk4N2mT4")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

try:
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception as e:
    st.error(f"Error crítico de conexión con Gemini: {e}")
    st.stop()

# 2. CONTEXTO CORPORATIVO DE NEXARA FINANCE
NEXARA_CONTEXT = """
Eres el Asistente Ejecutivo Central de Nexara Finance (Dirección Financiera Inteligente para Pymes).
Directora Fundadora: Luz Dalia Granados Diaz.

Servicios principales: 
- Plan A: Avanzado AI-Driven (450€/mes). Incluye Consultoría de Viabilidad, Auditoría Preventiva AI, Control de Tesorería (Cashflow) y Pool Bancario.
- Plan B: Reskate Financiero (Pago único + 450€/mes) para regularizar empresas con retrasos contables o impositivos.

Tono de voz: Empático, riguroso, directo, resolutivo. Nunca uses jerga corporativa vacía. Vincula soluciones a rentabilidad y cashflow.
Reglas de diseño: Azul corporativo (#185FA5). Verde solo para métricas positivas o CTAs.
"""

# 3. MÓDULO DE AUTENTICACIÓN Y GMAIL API
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly']

def obtener_servicio_gmail():
    """Maneja la autenticación OAuth 2.0 y la persistencia de sesión."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                st.error("⚠️ Error: No se encuentra 'credentials.json' en la raíz.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def enviar_correo_real(destinatario: str, asunto: str, cuerpo: str) -> str:
    """Envía el correo redactado a través de los servidores de Google."""
    try:
        service = obtener_servicio_gmail()
        if not service: return "Fallo en autenticación."
        
        mensaje = MIMEText(cuerpo)
        mensaje['to'] = destinatario
        mensaje['subject'] = asunto
        raw_message = base64.urlsafe_b64encode(mensaje.as_bytes()).decode('utf-8')
        
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        return f"✅ ¡Correo enviado con éxito a {destinatario}!"
    except Exception as e:
        return f"❌ Error en Gmail API: {str(e)}"

# 4. INTERFAZ OPERATIVA (DASHBOARD)
st.markdown("<h1 style='color: #185FA5; font-family: Sora, sans-serif;'>Nexara Finance · Centro de Control AI 24/7</h1>", unsafe_allow_html=True)
st.write(f"**Usuario Activo:** Gestión Granados | **Estrategia Corporativa Automatizada**")

tab1, tab2, tab3 = st.tabs(["📩 Gestión de Correos", "📈 Marketing Estratégico", "📅 Planificador de Reuniones"])

# TAB 1: GMAIL INTEGRATION
with tab1:
    st.subheader("Redacción y Envío Automatizado")
    col1, col2 = st.columns(2)
    
    with col1:
        destinatario = st.text_input("Para (Email del Cliente):", placeholder="ejemplo@pyme.com")
        instrucciones = st.text_area("¿Qué necesitas comunicar?", height=150)
        
        if st.button("Generar Borrador Inteligente"):
            if instrucciones:
                with st.spinner("Gemini redactando con tono Nexara..."):
                    response = client.models.generate_content(
                        model='gemini-2.0-flash',
                        contents=f"Redacta un correo: {instrucciones}",
                        config=types.GenerateContentConfig(system_instruction=NEXARA_CONTEXT, temperature=0.3)
                    )
                    st.session_state['borrador_actual'] = response.text

    with col2:
        if 'borrador_actual' in st.session_state:
            st.info("Revisa y edita antes de enviar")
            cuerpo_final = st.text_area("Contenido del Correo:", value=st.session_state['borrador_actual'], height=250)
            asunto_final = st.text_input("Asunto:", value="Comunicación Urgente - Nexara Finance")
            
            if st.button("🚀 ENVIAR CORREO AHORA"):
                if destinatario:
                    resultado = enviar_correo_real(destinatario, asunto_final, cuerpo_final)
                    st.success(resultado)
                else:
                    st.warning("Introduce un email de destino.")

# TAB 2: MARKETING
with tab2:
    st.subheader("Factoría de Contenido Nexara")
    canal = st.selectbox("Canal:", ["LinkedIn Corporativo", "Newsletter Pymes", "Scripts de Video"])
    sector = st.text_input("Sector objetivo:", "Distribución y Logística")
    
    if st.button("Estructurar Estrategia"):
        with st.spinner("Generando contenido estratégico..."):
            prompt = f"Crea contenido para {canal} enfocado en {sector}. Resalta el Plan A de Nexara."
            res_mkt = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=NEXARA_CONTEXT + "\nFinaliza con CTA para auditoría.",
                    temperature=0.7
                )
            )
            st.markdown("---")
            st.write(res_mkt.text)

# TAB 3: REUNIONES
with tab3:
    st.subheader("Actas y Minutas Automatizadas")
    notas = st.text_area("Pega aquí las notas de la reunión:")
    
    if st.button("Procesar Acta Formal"):
        if notas:
            with st.spinner("Estructurando puntos clave..."):
                res_meet = client.models.generate_content(
                    model='gemini-2.5-flash', # Mantenemos el modelo que solicitaste originalmente aquí
                    contents=f"Procesa esta acta: {notas}",
                    config=types.GenerateContentConfig(
                        system_instruction=NEXARA_CONTEXT + "\nFormato: 1. Puntos Clave, 2. Decisiones, 3. Tareas.",
                        temperature=0.2
                    )
                )
                st.info(res_meet.text)
