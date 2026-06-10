import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Inicialización directa y forzada
def init_nexara():
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("Error: GOOGLE_API_KEY no configurada.")
        st.stop()
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')

model = init_nexara()

# Motor autónomo
def ejecutar_tarea(tarea, contexto):
    try:
        prompt = f"Eres el Agente Autónomo Nexara. Riguroso y resolutivo. Tarea: {tarea}. Contexto: {contexto}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error en el motor: {str(e)}"

# Interfaz
st.title("🤖 Centro de Control Nexara Finance")
tab1, tab2, tab3 = st.tabs(["📩 Gestión", "📈 Marketing", "📅 Auditoría"])

with tab1:
    if st.button("Escanear Emails"):
        st.write(ejecutar_tarea("Analizar emails", "Pendiente de lectura"))

with tab2:
    if st.button("Generar Plan Semanal"):
        st.write(ejecutar_tarea("Generar contenido LinkedIn", "Enfoque: Ahorro fiscal Pymes"))

with tab3:
    notas = st.text_area("Datos financieros:")
    if st.button("Procesar Auditoría"):
        st.info(ejecutar_tarea("Detectar fugas financieras", notas))
