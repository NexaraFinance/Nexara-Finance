import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN E INICIALIZACIÓN ---
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Solo usamos la API KEY, nada de tokens externos
def init_agent():
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("Error: GOOGLE_API_KEY no encontrada en los secretos.")
        st.stop()
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')

model = init_agent()

# Esta es la esencia de Nexara: Riguroso, directo, empático y enfocado en resultados
NEXARA_IDENTITY = """
Eres el Asistente Ejecutivo de Nexara Finance, bajo la dirección de Luz Dalia Granados.
Tu estilo es:
1. Empático: Entiendes el estrés financiero del cliente.
2. Riguroso: Hablas con datos, no con promesas vacías.
3. Directo: Tu objetivo es invitar al cliente a una Auditoría Preventiva o al Plan Avanzado.
"""

def agente_nexara(tarea, input_usuario):
    try:
        response = model.generate_content(f"{NEXARA_IDENTITY}\nTarea: {tarea}\nInput: {input_usuario}")
        return response.text
    except Exception as e:
        return f"Error técnico: {str(e)}"

# --- INTERFAZ ---
st.title("💼 NEXARA FINANCE · Centro de Control Ejecutivo")

t1, t2, t3 = st.tabs(["📩 Gestión de Clientes", "📈 Marketing Estratégico", "📊 Auditoría Preventiva"])

with t1:
    st.subheader("Redacción de Propuestas")
    email_cliente = st.text_input("¿Qué problema presenta el cliente?")
    if st.button("Generar propuesta de rescate"):
        st.write(agente_nexara("Redacta un correo persuasivo para el cliente", email_cliente))

with t2:
    st.subheader("Contenido de Marca")
    tema = st.selectbox("Canal:", ["LinkedIn", "Blog Corporativo"])
    if st.button("Generar Post"):
        st.write(agente_nexara(f"Genera un post para {tema} sobre ahorro fiscal", "Resalta el valor de Nexara"))

with t3:
    st.subheader("Auditoría de Fugas")
    notas = st.text_area("Pega los datos del cliente aquí:")
    if st.button("Detectar oportunidades de ahorro"):
        st.info(agente_nexara("Analiza los datos, detecta fugas y propone soluciones", notas))
