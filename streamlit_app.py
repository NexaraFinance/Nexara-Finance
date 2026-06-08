import streamlit as st
import google.generativeai as genai

# Configuración de página (solo debe aparecer una vez)
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Configuración de la API usando st.secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    st.title("Nexara Finance - Centro de Control AI 24/7")
    st.write("Usuario Activo: Gestión Granados | Estrategia Corporativa Automatizada")
else:
    st.error("Error: La clave GOOGLE_API_KEY no se encuentra en los secretos.")

# --- CONTEXTO CORPORATIVO DE NEXARA FINANCE ---
NEXARA_CONTEXT = """
Eres el Asistente Ejecutivo Central de Nexara Finance (Dirección Financiera Inteligente para Pymes).
Directora Fundadora: Luz Dalia Granados Diaz.
Servicios principales: 
- Plan A: Avanzado AI-Driven (450€/mes). Incluye Consultoría de Viabilidad, Auditoría Preventiva AI, Control de Tesorería (Cashflow) y Pool Bancario.
- Plan B: Rescate Financiero (Pago único + 450€/mes) para regularizar empresas con retrasos contables o impositivos.
Tono de voz: Empático, riguroso, directo, resolutivo. Nunca uses jerga corporativa vacía ("añadir valor"). Vincula las soluciones a resultados concretos (ej: aumentar rentabilidad, controlar el cashflow).
Reglas de diseño de marca: El color verde solo se usa para métricas de datos positivos o CTAs fuertes. El color principal es el azul corporativo (#185FA5).
"""

# --- AUTENTICACIÓN Y MÓDULO GOOGLE GMAIL ---
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly']

def obtener_servicio_gmail():
    """Autentica al usuario mediante OAuth 2.0 y mantiene la sesión abierta 24/7 con token.json"""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                st.error("Por favor, coloca tu archivo 'credentials.json' descargado de Google Cloud Console en la raíz del proyecto.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def enviar_correo_real(destinatario: str, asunto: str, cuerpo: str) -> str:
    """Función de ejecución real: Envía un correo electrónico usando Gmail API."""
    try:
        service = obtener_servicio_gmail()
        if not service:
            return "Error de autenticación con Gmail."
        
        mensaje = MIMEText(cuerpo)
        mensaje['to'] = destinatario
        mensaje['subject'] = asunto
        raw_message = base64.urlsafe_b64encode(mensaje.as_bytes()).decode('utf-8')
        
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        return f"✅ ¡Correo enviado con éxito a {destinatario}!"
    except Exception as e:
        return f"❌ Fallo al enviar el correo a través de la API: {e}"

# --- INICIALIZACIÓN DE CLIENTES ---
# Se recomienda configurar tu GEMINI_API_KEY en tu entorno o en .streamlit/secrets.toml
try:
    client = genai.Client(api_key="Fk4N2mT4")
except Exception:
    st.error("API Key de Gemini no configurada. Añádela en tus variables de entorno.")
# --- INTERFAZ DEL DASHBOARD OPERATIVO ---
st.markdown("<h1 style='color: #185FA5; font-family: Sora, sans-serif;'>Nexara Finance · Centro de Control AI 24/7</h1>", unsafe_allow_html=True)
st.write(f"**Usuario Activo:** Gestión Granados | **Estrategia Corporativa Automatizada**")

tab1, tab2, tab3 = st.tabs(["📩 Gestión de Correos Inteligente", "📈 Factoría de Marketing Nexara", "📅 Planificador de Reuniones"])

# TAB 1: GESTIÓN DE CORREOS
with tab1:
    st.subheader("Redacción y Envío Automatizado")
    col_em1, col_em2 = col_em1, col_em2 = st.columns(2)
    
    with col_em1:
        destinatario = st.text_input("Para (Email del Cliente):", placeholder="cliente@pyme.com")
        instrucciones_correo = st.text_area(
            "¿Qué quieres comunicarle al cliente?", 
            placeholder="Ej: Recordarle al cliente del Plan B que necesitamos los extractos bancarios de marzo o se retrasará la auditoría de caja."
        )
    
    if st.button("Generar Borrador con Gemini"):
        if instrucciones_correo:
            with st.spinner("Gemini procesando tono y contexto de marca..."):
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"Redacta un correo basado en esto: {instrucciones_correo}. Recuerda el tono Nexara.",
                    config=types.GenerateContentConfig(
                        system_instruction=NEXARA_CONTEXT,
                        temperature=0.3
                    )
                )
                st.session_state['borrador_correo'] = response.text
                
    if 'borrador_correo' in st.session_state:
        with col_em2:
            st.markdown("gestiongranados@gmail.com | +34 915 985 222")
            cuerpo_editado = st.text_area("gestiongranados@gmail.com | +34 915 985 222:", value=st.session_state['borrador_correo'], height=250)
            asunto_mail = st.text_input("Línea de Asunto:", value="Actualización Urgente - Nexara Finance")
            
            if st.button("🚀 ENVIAR CORREO REAL AHORA VIA GMAIL API"):
                if destinatario:
                    resultado = enviar_correo_real(destinatario, asunto_mail, cuerpo_editado)
                    st.success(resultado)
                else:
                    st.warning("Por favor, introduce un correo de destino válido.")

# TAB 2: DASHBOARD DE MARKETING PULIDO
with tab2:
    st.subheader("Generador Estratégico de Contenido (Manual de Marca V2025)")
    st.info("Recordatorio de marca: Usar tipografía Sora para títulos, Inter para bloques informativos. Enfoque 100% en dolores del emprendedor.")
    
    canal = st.selectbox("Selecciona el Canal Objetivo:", ["LinkedIn Corporativo", "Newsletter para Pymes", "Script para Video Corto (Reels/TikTok)"])
    audiencia_objetivo = st.text_input("Sector de la Pyme objetivo:", value="Empresas de distribución y logística, comercio minorista")
    
    if st.button("Estructurar Estrategia de Contenido"):
        with st.spinner("Analizando pilares de comunicación de Nexara..."):
            prompt_marketing = f"Genera una pieza de contenido premium para {canal}, dirigida al sector de {audiencia_objetivo}. Destaca los beneficios del Plan A de automatización financiera o el peligro de no tener controlado el flujo de caja diario."
            
            response_mkt = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt_marketing,
                config=types.GenerateContentConfig(
                    system_instruction=NEXARA_CONTEXT + "\nRegla estricta: Termina siempre el post con una CTA o pregunta sumamente clara enfocada a agendar una auditoría preventiva, tal como exige el manual de marca.",
                    temperature=0.7
                )
            )
            st.markdown("### 📋 Copy Estratégico Generado")
            st.write(response_mkt.text)

# TAB 3: ORGANIZACIÓN DE REUNIONES
with tab3:
    st.subheader("Minutas de Reuniones y Planificación Automatizada")
    notas_caoticas = st.text_area("Pega aquí tus notas rápidas tomadas durante una reunión o llamada de diagnóstico:")
    
    if st.button("Procesar Acta de Reunión"):
        if notas_caoticas:
            with st.spinner("Estructurando puntos de acción..."):
                response_meet = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"Transforma estas notas en un acta formal de Nexara Finance: {notas_caoticas}",
                    config=types.GenerateContentConfig(
                        system_instruction=NEXARA_CONTEXT + "\nOrganiza la salida exactamente en: 1. Puntos Clave Analizados, 2. Decisiones de Control Financiero Tomadas, 3. Tareas Pendientes con Responsables Asignados.",
                        temperature=0.2
                    )
                )
                st.markdown("### 📅 Plan de Acción y Siguientes Pasos")
                st.info(response_meet.text)
