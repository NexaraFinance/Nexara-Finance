import streamlit as st
import google.generativeai as genai
import os

# 1. Configuración de página
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# 2. Inicialización Crítica
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("❌ ERROR: GOOGLE_API_KEY no encontrada en los secretos.")
    st.stop()

# Usamos la librería clásica y estable
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Motor Autónomo (Backend)
def motor_agente_nexara(tarea, datos):
    system_instruction = "Eres el Agente Autónomo Nexara. Analiza fugas financieras, redacta propuestas y agenda reuniones. Sé riguroso y resolutivo."
    try:
        response = model.generate_content(f"{system_instruction}\nTarea: {tarea}\nDatos: {datos}")
        return response.text
    except Exception as e:
        return f"Error en el motor: {str(e)}"

# 4. Interfaz del Centro de Control
st.markdown("# 🤖 Centro de Control Nexara Finance")
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
    notas = st.text_area("Datos financieros para analizar:")
    if st.button("Procesar Estado Financiero"):
        st.info(motor_agente_nexara("Detectar fugas en balance", notas))
