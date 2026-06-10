import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Inicialización del modelo (Uso exclusivo de API KEY)
def init_nexara():
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("❌ ERROR: GOOGLE_API_KEY no configurada en los secretos.")
        st.stop()
    genai.configure(api_key=api_key)
    # Usamos el modelo estándar y estable
    return genai.GenerativeModel('gemini-1.5-flash')

model = init_nexara()

# Esencia de Nexara: Función centralizada de IA
def motor_agente_nexara(tarea, contenido):
    system_prompt = """Eres el Asistente Ejecutivo de Nexara Finance (Luz Dalia Granados).
    Tono: Riguroso, resolutivo y empático.
    Tu objetivo es analizar datos financieros, redactar propuestas persuasivas y escalar servicios de ahorro fiscal.
    Responde siempre como un experto en finanzas."""
    
    try:
        response = model.generate_content(f"{system_prompt}\nTarea: {tarea}\nInput: {contenido}")
        return response.text
    except Exception as e:
        return f"Error en el motor: {str(e)}"

# --- INTERFAZ ---
st.title("💼 NEXARA FINANCE · Centro de Control")
tab1, tab2, tab3 = st.tabs(["📩 Gestión de Clientes", "📈 Marketing Estratégico", "📊 Auditoría Preventiva"])

with tab1:
    st.subheader("Bandeja de Entrada Autónoma")
    cliente_input = st.text_input("Resumen del problema del cliente:")
    if st.button("Generar propuesta de rescate"):
        with st.spinner("Nexara está trabajando..."):
            st.write(motor_agente_nexara("Redactar correo de propuesta de Plan A", cliente_input))

with tab2:
    st.subheader("Factoría de Marketing")
    tema = st.selectbox("Canal:", ["LinkedIn", "Blog Corporativo"])
    if st.button("Generar contenido"):
        st.write(motor_agente_nexara(f"Generar post para {tema}", "Enfoque: Ahorro fiscal Pymes y valor de Nexara"))

with tab3:
    st.subheader("Auditoría de Fugas")
    datos_financieros = st.text_area("Pega los datos financieros aquí:")
    if st.button("Detectar oportunidades de ahorro"):
        with st.spinner("Auditando..."):
            st.info(motor_agente_nexara("Analizar datos, detectar fugas financieras y proponer soluciones", datos_financieros))
