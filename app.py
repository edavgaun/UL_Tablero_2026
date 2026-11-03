import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="UL Tablero 2026", layout="wide")

# Título del panel de control en la barra lateral
st.sidebar.title("Panel de Control")
st.sidebar.write("Navegación del tablero")

# Lista de las 7 actividades
actividades = [
    "Actividad 1: Resumen General",
    "Actividad 2: Carga de Archivos",
    "Actividad 3: Análisis de Datos",
    "Actividad 4: Gráficos Interactivos",
    "Actividad 5: Procesamiento",
    "Actividad 6: Generación de Reportes",
    "Actividad 7: Configuración"
]

# Widget de selección en la barra lateral
seleccion = st.sidebar.radio("Selecciona una actividad:", actividades)

# Título principal de la app
st.title("UL Tablero 2026")
st.markdown("---")

# Placeholders para cada actividad
if seleccion == "Actividad 1: Resumen General":
    st.header("📊 Resumen General")
    st.write("Este es el placeholder para la Actividad 1. Aquí puedes poner métricas clave (st.metric) o una introducción al tablero.")

elif seleccion == "Actividad 2: Carga de Archivos":
    st.header("📂 Carga de Archivos")
    st.write("Este es el placeholder para la Actividad 2. Ideal para usar st.file_uploader() y cargar CSVs o Excel.")
    # ejemplo_archivo = st.file_uploader("Sube un archivo aquí")

elif seleccion == "Actividad 3: Análisis de Datos":
    st.header("🔍 Análisis de Datos")
    st.write("Este es el placeholder para la Actividad 3. Aquí puedes mostrar tablas de datos usando st.dataframe().")

elif seleccion == "Actividad 4: Gráficos Interactivos":
    st.header("📈 Gráficos Interactivos")
    st.write("Este es el placeholder para la Actividad 4. Espacio reservado para st.line_chart, st.bar_chart o gráficos de Plotly/Altair.")

elif seleccion == "Actividad 5: Procesamiento":
    st.header("⚙️ Procesamiento de Datos")
    st.write("Este es el placeholder para la Actividad 5. Aquí puedes colocar botones (st.button) que ejecuten scripts o cálculos pesados.")

elif seleccion == "Actividad 6: Generación de Reportes":
    st.header("📄 Generación de Reportes")
    st.write("Este es el placeholder para la Actividad 6. Útil para mostrar resultados finales y botones de descarga (st.download_button).")

elif seleccion == "Actividad 7: Configuración":
    st.header("🛠️ Configuración")
    st.write("Este es el placeholder para la Actividad 7. Aquí puedes incluir sliders, text_inputs y ajustes generales de la aplicación.")

# Pie de página en el sidebar
st.sidebar.markdown("---")
st.sidebar.caption("Repositorio: UL_Tablero_2026")
