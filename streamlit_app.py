import streamlit as st
from google import genai
from google.genai import types

# 1. Configuración de página
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# 2. Inicialización Crítica (Cargamos la clave desde los secretos de Streamlit)
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ ERROR: No se ha configurado la 'GOOGLE_API_KEY' en los secretos de Streamlit.")
    st.stop()

# Inicializamos el cliente. 
# Si esto da error, el problema es la API KEY o los permisos en Google AI Studio.
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"❌ Error al inicializar el cliente: {e}")
    st.stop()

# 3. Interfaz
st.title("Nexara Finance · Centro de Control IA 24/7")
tab1, tab2, tab3 = st.tabs(["📩 Gestión", "📈 Marketing", "📅 Reuniones"])

with tab1:
    st.subheader("Comunicación Inteligente")
    instr = st.text_area("¿Qué quieres comunicarle al cliente?")
    if st.button("Generar Borrador"):
        try:
            # Usamos el modelo más estable disponible
            resp = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=instr,
                config=types.GenerateContentConfig(
                    system_instruction="Eres el asistente de Nexara Finance. Directora: Luz Dalia Granados. Tono empático, riguroso y resolutivo."
                )
            )
            st.write(resp.text)
        except Exception as e:
            st.error(f"❌ Error al conectar con Gemini: {e}")

with tab2:
    st.subheader("Factoría de Marketing")
    if st.button("Generar Post de LinkedIn"):
        resp = client.models.generate_content(model='gemini-1.5-flash', contents="Crea un post de LinkedIn sobre ahorro fiscal para pymes.")
        st.write(resp.text)

with tab3:
    st.subheader("Procesamiento de Actas")
    notas = st.text_area("Notas:")
    if st.button("Procesar"):
        resp = client.models.generate_content(model='gemini-1.5-flash', contents=f"Resume: {notas}")
        st.info(resp.text)
