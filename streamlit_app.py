import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Configuración de Gemini desde Secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("Error en la configuración de la API Key. Verifica tus 'Secrets' en Streamlit.")

def analizar_cliente():
    st.header("📊 Análisis de Cliente: Nexara Finance")
    datos = st.text_area("Pega aquí los datos financieros del cliente:", height=250)
    
    if st.button("Generar Diagnóstico Estratégico"):
        if datos:
            try:
                with st.spinner('El cerebro de Nexara Finance está analizando...'):
                    prompt = f"""
                    Actúa como un Consultor Financiero Sénior. Analiza estos datos: {datos}.
                    Proporciona: 1. Diagnóstico Ejecutivo, 2. Alerta de Riesgos, 3. Hoja de Ruta (3 pasos).
                    Mantén un tono profesional y enfocado en PYMES.
                    """
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Ocurrió un error al conectar con la IA: {e}")
        else:
            st.warning("Por favor, introduce los datos.")

# Menú lateral
menu = ["Inicio", "Análisis de Cliente"]
opcion = st.sidebar.selectbox("Selecciona tu área de trabajo:", menu)

if opcion == "Análisis de Cliente":
    analizar_cliente()
else:
    st.write("Bienvenida a Nexara Finance OS.")
    
