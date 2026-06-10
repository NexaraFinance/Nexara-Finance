import streamlit as st
from google import genai
from google.genai import types

# ESTE MÓDULO SE EJECUTA AUTOMÁTICAMENTE
def motor_autonomo_nexara(datos_cliente):
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
    
    # Análisis Autónomo (IA)
    evaluacion = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=f"Analiza estos datos financieros: {datos_cliente}",
        config=types.GenerateContentConfig(
            system_instruction="Eres el Agente Autónomo Nexara. Detecta si hay fugas. Si las hay, redacta una propuesta de Plan B y un CTA para agendar auditoría."
        )
    )
    return evaluacion.text

# --- INTEGRACIÓN CON EL DASHBOARD ---
st.title("🚀 Nexara Autonomous Dashboard")
st.info("El sistema está monitorizando tus flujos de entrada.")

if st.button("Ejecutar Escaneo de Clientes (Modo Autónomo)"):
    with st.spinner("El Agente Nexara está procesando cuentas..."):
        # Aquí conectarías con tu base de datos o Gmail
        datos_demo = "Facturas de proveedor X duplicadas, falta de deducción de IVA en transporte."
        informe = motor_autonomo_nexara(datos_demo)
        st.write("### Informe Generado por el Agente:")
        st.write(informe)
        
        if st.button("Aprobar Envío Automático"):
            st.success("Propuesta enviada al cliente.")
