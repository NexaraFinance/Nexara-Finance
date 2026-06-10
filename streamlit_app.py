import os
import base64
import streamlit as st
from email.mime.text import MIMEText
from google import genai
from google.genai import types
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# --- INICIALIZACIÓN DE SERVICIOS ---
# 1. Validación de API KEY
api_key = st.secrets.get("GOOGLE_API_KEY") or st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ Configura GOOGLE_API_KEY en los secretos de Streamlit.")
    st.stop()

# 2. Cliente de IA
client = genai.Client(api_key=api_key)

# 3. Contexto Corporativo
NEXARA_CONTEXT = """Eres el Asistente Ejecutivo Central de Nexara Finance. 
Directora: Luz Dalia Granados Diaz. 
Tono: Empático, riguroso, directo. 
Servicios: Plan Avanzado (450€/mes), Rescate Financiero, Auditoría Preventiva AI.
Regla de Oro: Siempre vincula soluciones a beneficios económicos concretos. Finaliza propuestas con invitación a diagnóstico."""

# --- FUNCIONES DE SOPORTE ---
def enviar_correo_real(destinatario, asunto, cuerpo):
    try:
        # Nota: Asegúrate de tener el archivo token.json en la carpeta raíz
        creds = Credentials.from_authorized_user_file('token.json')
        service = build('gmail', 'v1', credentials=creds)
        mensaje = MIMEText(cuerpo)
        mensaje['to'] = destinatario
        mensaje['subject'] = asunto
        raw = base64.urlsafe_b64encode(mensaje.as_bytes()).decode('utf-8')
        service.users().messages().send(userId='me', body={'raw': raw}).execute()
        return True, "✅ Correo enviado con éxito."
    except Exception as e:
        return False, f"❌ Error: {str(e)}"

# --- INTERFAZ CENTRAL (TABS) ---
st.markdown("<h1 style='color: #185FA5;'>Nexara Finance · Centro de Control IA</h1>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["📩 Gestión de Correos", "📈 Factoría de Marketing", "📅 Planificador de Reuniones"])

with tab1:
    st.subheader("Gestión de Comunicación Cliente")
    dest = st.text_input("Email del Cliente:", key="t1_dest")
    instr = st.text_area("Instrucciones para el borrador:", key="t1_instr")
    if st.button("Generar Borrador"):
        with st.spinner("Creando mensaje con sello Nexara..."):
            resp = client.models.generate_content(model='gemini-1.5-flash', contents=instr, 
                    config=types.GenerateContentConfig(system_instruction=NEXARA_CONTEXT))
            st.session_state['borrador'] = resp.text
    if 'borrador' in st.session_state:
        cuerpo = st.text_area("Borrador editable:", value=st.session_state['borrador'], height=200)
        if st.button("ENVIAR CORREO"):
            exito, mensaje = enviar_correo_real(dest, "Comunicación desde Nexara Finance", cuerpo)
            if exito: st.success(mensaje)
            else: st.error(mensaje)

with tab2:
    st.subheader("Generador de Contenido Estratégico")
    canal = st.selectbox("Canal:", ["LinkedIn", "Newsletter", "Video Corto"])
    sector = st.text_input("Sector objetivo:", "Distribución")
    if st.button("Estructurar Estrategia"):
        resp = client.models.generate_content(model='gemini-1.5-flash', 
                contents=f"Crea contenido para {canal} enfocado en {sector}.",
                config=types.GenerateContentConfig(system_instruction=NEXARA_CONTEXT))
        st.write(resp.text)

with tab3:
    st.subheader("Procesamiento de Actas")
    notas = st.text_area("Pega tus notas de reunión:")
    if st.button("Procesar Acta Formal"):
        resp = client.models.generate_content(model='gemini-1.5-flash', 
                contents=f"Crea acta formal de Nexara Finance: {notas}",
                config=types.GenerateContentConfig(system_instruction=NEXARA_CONTEXT))
        st.info(resp.text)
