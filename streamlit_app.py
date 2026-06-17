import streamlit as st

# Configuración básica de la aplicación
st.set_page_config(page_title="Nexara Finance OS", layout="wide")

# Título y bienvenida
st.title("📊 Nexara Finance OS")
st.subheader("Centro de Control y Gestión Estratégica")

# Menú lateral para navegar
menu = ["Inicio", "Gestión", "Marketing", "Reuniones", "Análisis de Cliente"]
opcion = st.sidebar.selectbox("Selecciona tu área de trabajo:", menu)

# Lógica de navegación
if opcion == "Análisis de Cliente":
    st.header("📊 Análisis de Cliente")
    st.write("Copia aquí los datos extraídos de la contabilidad del cliente para generar un diagnóstico estratégico.")
    
    datos = st.text_area("Datos financieros (Balance/P&L/Cash Flow):", height=250)
    
    if st.button("Generar Diagnóstico Estratégico"):
        if datos:
            st.info("Procesando datos con los estándares de Nexara Finance...")
            # Aquí añadiremos la inteligencia de Gemini en el siguiente paso
            st.write("---")
            st.subheader("Informe de Diagnóstico")
            st.write("El sistema analizará: Liquidez, Rentabilidad y Solvencia.")
        else:
            st.warning("Por favor, pega los datos del cliente primero.")

elif opcion == "Inicio":
    st.write("Bienvenida al sistema operativo de Nexara Finance. Selecciona una herramienta en el menú lateral para comenzar a trabajar.")

else:
    st.write(f"Módulo de {opcion} en construcción.")
