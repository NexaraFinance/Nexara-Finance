import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# 1. Configuración Estricta (Solo API Key)
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("Configura GOOGLE_API_KEY en los secretos.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Función de Ejecución Pura
def procesar_nexara(tarea, datos):
    try:
        response = model.generate_content(f"Agente Nexara Finance. Tarea: {tarea}. Datos: {datos}")
        return response.text
    except Exception as e:
        return f"Error: {e}"

# 3. Interfaz de Negocio
st.title("💼 Nexara Finance: Gestión Autónoma")
tab1, tab2, tab3 = st.tabs(["📩 Gestión", "📈 Marketing", "📊 Auditoría"])

with tab1:
    st.write("Automatización de respuesta a clientes")
    if st.button("Escanear y Responder"):
        st.write(procesar_nexara("Redactar email de seguimiento", "Cliente pide info de Plan A"))

with tab2:
    st.write("Factoría de Marketing")
    if st.button("Generar Post"):
        st.write(procesar_nexara("Crear post de ahorro fiscal", "Enfoque Nexara"))

with tab3:
    st.write("Auditoría de Fugas")
    if st.button("Detectar Oportunidades"):
        st.info(procesar_nexara("Analizar fugas financieras", "Gastos operativos altos"))
