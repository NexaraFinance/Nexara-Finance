import os
import base64
import streamlit as st
from email.mime.text import MIMEText
import google.generativeai as genai

# Integración oficial de la API de Gmail de Google
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Configuración visual de Streamlit con la paleta Nexara Finance
st.set_page_config(page_title="Nexara Finance OS - Centro de Control AI", layout="wide")

# --- CONTEXTO CORPORATIVO (Optimizado para evitar errores de codificación) ---
NEXARA_CONTEXT = (
    "Eres el Asistente Ejecutivo Central de Nexara Finance (Dirección Financiera Inteligente para Pymes). "
    "Directora Fundadora: Luz Dalia Granados Diaz. "
    "Servicios principales: "
    "Plan A: Avanzado AI-Driven (450 euros/mes). Incluye Consultoría de Viabilidad, Auditoría Preventiva AI, Control de Tesorería (Cashflow) y Pool Bancario. "
    "Plan B: Rescate Financiero (Pago único + 450 euros/mes) para regularizar empresas con retrasos contables o impositivos. "
    "Tono de voz: Empático, riguroso, directo, resolutivo. Nunca uses jerga corporativa vacía. Vincula las soluciones a resultados concretos. "
    "Reglas de diseño de marca: El color verde solo se usa para métricas de datos positivos o CTAs fuertes. El color principal es el azul corporativo (#185FA5)."
)

# --- CONFIGURACIÓN DE LA API KEY ---
if "GOOGLE_API_KEY" in st.secrets:
    GEMINI_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    GEMINI_KEY = "Fk4N2mT4"  # Tu clave por defecto

genai.configure(api_key=GEMINI_KEY)

# --- AUTENTICACIÓN Y MÓDULO GOOGLE GMAIL ---
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly']

def obtener_servicio_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                st.error("Por favor, coloca tu archivo 'credentials.json' en la raíz del proyecto.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def enviar_correo_real(destinatario: str, asunto: str, cuerpo: str) -> str:
    try:
        service = obtener_servicio_gmail()
        if not service:
            return "Error de autenticación con Gmail."
        mensaje = MIMEText(cuerpo)
        mensaje['to'] = destinatario
        mensaje['subject'] = asunto
        raw_message = base64.urlsafe_b64encode(mensaje.as_bytes()).decode('utf-8')
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        return f"Corrientemente enviado a {destinatario}"
    except Exception as e:
        return f"Error al enviar: {e}"

# --- INTERFAZ DEL DASHBOARD ---
st.markdown("<h1 style='color: #185FA5; font-family: Sora, sans-serif;'>Nexara Finance · Centro de Control AI 24/7</h1>", unsafe_allow_html=True)
st.write("**Usuario Activo:** Gestión Granados | **Estrategia Corporativa Automatizada**")

tab1, tab2, tab3 = st.tabs(["📩 Gestión de Correos Inteligente", "📈 Factoría de Marketing Nexara", "📅 Planificador de Reuniones"])

# TAB 1: GESTIÓN DE CORREOS
with tab1:
    st.subheader("Redacción y Envío Automatizado")
    col_em1, col_em2 = st.columns(2)
    
    with col_em1:
        destinatario = st.text_input("Para (Email del Cliente):", placeholder="cliente@pyme.com", key="mail_dest")
        instrucciones_correo = st.text_area("¿Qué quieres comunicarle al cliente?", placeholder="Ej: Recordarle los extractos...", key="mail_inst")
        
        if st.button("Generar Borrador con Gemini", key="btn_gen_mail"):
            if instrucciones_correo:
                with st.spinner("Procesando..."):
                    model = genai.GenerativeModel(
                        model_name='gemini-1.5-flash',
                        system_instruction=NEXARA_CONTEXT
                    )
                    response = model.generate_content(f"Redacta un correo directo basado en esto: {instrucciones_correo}")
                    st.session_state['borrador_correo'] = response.text
                
    with col_em2:
        if 'borrador_correo' in st.session_state:
            st.markdown("**Remitente:** gestiongranados@gmail.com")
            cuerpo_editado = st.text_area("Contenido:", value=st.session_state['borrador_correo'], height=250, key="mail_body")
            asunto_mail = st.text_input("Asunto:", value="Actualización Urgente - Nexara Finance", key="mail_asunto")
            
            if st.button("🚀 ENVIAR CORREO REAL VIA GMAIL", key="btn_send_gmail"):
                if destinatario:
                    resultado = enviar_correo_real(destinatario, asunto_mail, cuerpo_editado)
                    st.success(resultado)
                else:
                    st.warning("Introduce un correo válido.")

# TAB 2: MARKETING
with tab2:
    st.subheader("Generador Estratégico de Contenido")
    canal = st.selectbox("Canal:", ["LinkedIn Corporativo", "Newsletter", "Script Video Corto"], key="mkt_canal")
    audiencia = st.text_input("Sector Pyme:", value="Logística y Distribución", key="mkt_aud")
    
    if st.button("Estructurar Estrategia", key="btn_mkt"):
        with st.spinner("Analizando..."):
            model = genai.GenerativeModel(
                model_name='gemini-1.5-flash',
                system_instruction=NEXARA_CONTEXT + " Termina siempre con un CTA claro para agendar una auditoría preventiva."
            )
            prompt = f"Genera un contenido premium para {canal} enfocado en el sector de {audiencia} sobre la gestión del flujo de caja."
            response_mkt = model.generate_content(prompt)
            st.markdown("### Copy Generado")
            st.write(response_mkt.text)

# TAB 3: REUNIONES
with tab3:
    st.subheader("Minutas de Reuniones")
    notas = st.text_area("Notas rápidas de la reunión:", key="meet_notes")
    
    if st.button("Procesar Acta", key="btn_meet"):
        if notas:
            with st.spinner("Estructurando..."):
                model = genai.GenerativeModel(
                    model_name='gemini-1.5-flash',
                    system_instruction=NEXARA_CONTEXT + " Organiza la salida exactamente en: 1. Puntos Clave, 2. Decisiones de Control Tomadas, 3. Tareas Pendientes."
                )
                response_meet = model.generate_content(f"Estructura estas notas: {notas}")
                st.info(response_meet.text)
