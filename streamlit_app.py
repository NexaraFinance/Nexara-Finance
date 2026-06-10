import streamlit as st
from google import genai
from google.genai import types
import time

# --- CONFIGURACIÓN E INICIALIZACIÓN ---
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Inicialización del cliente con manejo de errores robusto
def get_client():
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not api_key: st.stop()
    return genai.Client(api_key=api_key)

client = get_client()

# --- MOTOR DE AUTOMATIZACIÓN (AGENTE AUTÓNOMO) ---
def motor_agente_nexara(tarea, datos):
    """
    Este es el 'cerebro' que trabaja solo. 
    Llamado por los módulos de gestión, marketing y auditoría.
    """
    system_prompt = """Eres el Agente Autónomo Nexara. 
    Tu objetivo: Detectar fugas financieras, redactar propuestas comerciales y agendar reuniones.
    Actúa sin intervención humana: analiza, propone y ejecuta."""
    
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=f"Tarea: {tarea}. Datos: {datos}",
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )
    return response.text

# --- DASHBOARD DE CONTROL ---
st.title("🤖 Centro de Control Nexara Finance")
st.sidebar.success("Estado: Sistema de Agente Autónomo Activo")

col1, col2 = st.columns([2, 1])

with col1:
    tab1, tab2, tab3 = st.tabs(["📩 Gestión", "📈 Marketing", "📅 Auditoría"])
    
    with tab1:
        st.subheader("Bandeja de Entrada Autónoma")
        if st.button("Escanear Emails de Clientes"):
            st.write(motor_agente_nexara("Analizar emails recibidos", "Pendiente de lectura en Gmail"))
            
    with tab2:
        st.subheader("Factoría de Contenido")
        if st.button("Generar Publicaciones Semanales"):
            st.write(motor_agente_nexara("Generar 5 posts para LinkedIn", "Enfoque: Ahorro fiscal Pymes"))
            
    with tab3:
        st.subheader("Auditoría Preventiva")
        if st.button("Procesar Estado Financiero"):
            st.write(motor_agente_nexara("Detectar fugas en balance", "Datos financieros actuales"))

with col2:
    st.subheader("Log de Actividad")
    # Aquí puedes guardar y mostrar los resultados de las tareas autónomas
    st.info("El sistema está procesando las tareas en segundo plano...")
