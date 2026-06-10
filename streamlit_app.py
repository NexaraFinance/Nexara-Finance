import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Inicialización Directa
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY no encontrada en los secretos.")
    st.stop()

# Configuración estricta de la API
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def motor_nexara(tarea, datos):
    try:
        # Instrucción de sistema para mantener la esencia de Nexara
        prompt = f"""Eres el Asistente Ejecutivo de Nexara Finance. 
        Tono: Profesional, riguroso, empático. 
        Objetivo: Detectar fugas financieras y proponer el Plan Avanzado.
        Tarea: {tarea}. Datos: {datos}"""
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error en el sistema: {str(e)}"

# Interfaz
st.title("💼 NEXARA FINANCE · Centro de Control")
tab1, tab2, tab3 = st.tabs(["📩 Gestión", "📈 Marketing", "📊 Auditoría"])

with tab1:
    if st.button("Escanear y Responder"):
        st.write(motor_nexara("Responder a cliente interesado", "El cliente pregunta por el Plan A"))

with tab2:
    if st.button("Generar Post"):
        st.write(motor_nexara("Post de LinkedIn sobre ahorro fiscal", "Enfoque Nexara"))

with tab3:
    notas = st.text_area("Datos para auditar:")
    if st.button("Procesar"):
        st.info(motor_nexara("Detectar fugas", notas))
