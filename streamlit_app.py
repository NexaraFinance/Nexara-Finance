import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE NÚCLEO ---
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Inicialización forzada mediante API KEY exclusivamente
def conectar_nexara():
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("Error: La llave de acceso (API_KEY) no está en los secretos.")
        st.stop()
    genai.configure(api_key=api_key)
    # Usamos la versión más estable del modelo
    return genai.GenerativeModel('gemini-1.5-flash')

model = conectar_nexara()

# --- LA ESENCIA: AGENTE NEXARA ---
def agente_nexara(tarea, datos):
    # La esencia: Luz Dalia Granados, experta en optimización financiera
    contexto = """Eres el Agente Autónomo de Nexara Finance. 
    Tu misión: Maximizar la rentabilidad de clientes PYME, detectar fugas de tesorería y escalar servicios. 
    Tono: Riguroso, humano, resolutivo. Enfócate siempre en el ahorro fiscal y la eficiencia."""
    
    try:
        response = model.generate_content(f"{contexto}\n\nTarea: {tarea}\nDatos: {datos}")
        return response.text
    except Exception as e:
        return f"Error en el motor: {str(e)}"

# --- UI: CENTRO DE CONTROL ---
st.title("💼 NEXARA FINANCE · Centro de Control Ejecutivo")

t1, t2, t3 = st.tabs(["📩 Gestión de Clientes", "📈 Marketing Estratégico", "📊 Auditoría Preventiva"])

with t1:
    st.subheader("Bandeja de Entrada Autónoma")
    input_cliente = st.text_input("¿Qué comunica el cliente?")
    if st.button("Generar propuesta de rescate"):
        st.write(agente_nexara("Redacta propuesta de Plan A (Ahorro Fiscal)", input_cliente))

with t2:
    st.subheader("Factoría de Marketing")
    if st.button("Generar Plan de Crecimiento"):
        st.write(agente_nexara("Crea 5 posts para LinkedIn sobre ahorro fiscal", "Enfoque Nexara"))

with t3:
    st.subheader("Auditoría Preventiva")
    notas = st.text_area("Datos de auditoría:")
    if st.button("Procesar Informe de Fugas"):
        st.info(agente_nexara("Analiza los datos y detecta fugas de dinero", notas))
