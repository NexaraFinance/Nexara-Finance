import streamlit as st
import os
# Usamos la librería oficial de Google AI
from google import genai

# 1. Configuración de página
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# 2. Inicialización Crítica
# Forzamos la lectura directa desde los secretos
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ ERROR: No se ha configurado la 'GOOGLE_API_KEY' en los secretos de Streamlit.")
    st.stop()

# Inicializamos el cliente pasando la clave explícitamente para evitar conflictos de autenticación
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"❌ Error al inicializar el cliente: {e}")
    st.stop()

# 3. Interfaz
st.title("🤖 Centro de Control Nexara Finance")
tab1, tab2, tab3 = st.tabs(["📩 Gestión", "📈 Marketing", "📅 Auditoría"])

# Motor autónomo simplificado
def motor_agente_nexara(tarea, datos):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Tarea: {tarea}. Datos: {datos}",
            config={"system_instruction": "Eres el Agente Autónomo Nexara. Riguroso, directo y resolutivo."}
        )
        return response.text
    except Exception as e:
        return f"Error en el motor: {str(e)}"

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
