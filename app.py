import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# ---------------------- CONFIGURACIÓN ----------------------
PALETA_COLORES = [
    "#E63946", "#8fbae5", "#A8DADC", "#457B9D", "#2A9D8F",
    "#264653", "#FF6F61", "#6A0572", "#FF9F1C", "#A6032F"
]
EMOCIONES = ["joy", "sadness", "surprise", "anger", "fear", "disgust"]
TRADUCIR_EMOCIONES = {
    "joy": "Alegría", "sadness": "Tristeza", "surprise": "Sorpresa",
    "anger": "Enojo", "fear": "Miedo", "disgust": "Disgusto"}
TRADUCIR_SENTIMIENTO = {"🔴": "Negativo", "🟡": "Neutro", "🟢": "Positivo"}
COLORES_LINEAS = {"🔴": "#E63946", "🟡": "#F4D35E", "🟢": "#2A9D8F"}

# ---------------------- CARGAR DATOS ----------------------
@st.cache_data(show_spinner=False)
def load_data():
    df = pd.read_csv("noticias_final_2.csv")
    df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d", errors="coerce")
    return df

if st.sidebar.button("🔄 Recargar datos"):
    st.cache_data.clear()

df = load_data()
if df.empty:
    st.error("No se encontraron noticias.")
    st.stop()

# ---------------------- LIMPIEZA ----------------------
df = df.drop_duplicates(subset="url")
df = df[df["fecha"].notna()]
df = df.sort_values("fecha", ascending=False)

# ---------------------- FILTROS ----------------------
st.sidebar.header("📅 Filtro de Temporalidad")
hoy = datetime.now()
opciones = {
    "Hoy": hoy.replace(hour=0, minute=0, second=0, microsecond=0),
    "Últimos 7 días": hoy - timedelta(days=7),
    "Últimos 30 días": hoy - timedelta(days=30),
    "Últimos 90 días": hoy - timedelta(days=90),
    "Histórico": None
}
seleccion = st.sidebar.selectbox("Selecciona un periodo:", list(opciones.keys()))
if opciones[seleccion]:
    fecha_min = opciones[seleccion]
    df = df[df["fecha"] >= fecha_min]

# Diagnóstico para verificar fechas filtradas
if not df.empty:
    st.write(f"📅 Noticias filtradas: {df['fecha'].min().date()} → {df['fecha'].max().date()}")
    st.write(f"🧮 Total de noticias mostradas: {len(df)}")
else:
    st.warning("⚠️ No hay noticias para este periodo.")

# ---------------------- FILTROS ADICIONALES ----------------------
st.sidebar.header("📂 Categoría")
categoria = st.sidebar.radio("Categoría:", ["Gobierno", "Alcalde", "Congreso", "Seguridad"], horizontal=True)
if categoria == "Gobierno":
    subcats = [
        "Ejecutiva", "Ayuntamiento", "Contraloría", "Seguridad y Protección Ciudadana",
        "Desarrollo Económico", "Servicios Públicos", "Desarrollo Urbano", "Infraestructura Sostenible",
        "Desarrollo Humano e Igualdad Sustantiva", "Innovación y Gobierno Abierto",
        "DIF Mty", "IMMR", "INJURE", "IMPLANC"
    ]
    sub = st.sidebar.selectbox("Subcategoría:", subcats)
    df = df[df["subpestaña"] == sub]
else:
    df = df[df["pestaña"] == categoria]

query = st.sidebar.text_input("🔍 Buscar texto:")
if query:
    df = df[df["texto_completo"].str.contains(query, case=False, na=False)]

# ---------------------- ESTILOS Y BANNER ----------------------
st.markdown("""
<style>
.banner {
    background: linear-gradient(to right, #E63946, #457B9D);
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: bold;
    font-size: 26px;
    border-radius: 10px;
    margin-bottom: 20px;
}
.noticia-card {
    width: 100%;
    background-color: #f9f9f9;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    font-family: sans-serif;
    margin-bottom: 1rem;
}
.noticia-card h4 { font-size: 15px; }
.noticia-card p { font-size: 13px; color: #333; }
.noticia-card .fecha { font-size: 12px; color: #777; }
.noticia-card .hashtag { font-size: 12px; color: #457B9D; font-weight: bold; }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="banner">Noticias del Gobierno de Monterrey</div>', unsafe_allow_html=True)

# ---------------------- NOTICIAS EN DOS COLUMNAS ----------------------
st.markdown("## 📰 Noticias Recientes")
col1, col2 = st.columns(2)
for i, (_, row) in enumerate(df.iterrows()):
    fecha_str = row["fecha"].strftime("%Y-%m-%d")
    hashtag = row["hashtag_diccionario"] if pd.notnull(row["hashtag_diccionario"]) else ""
    card_html = f"""
        <div class="noticia-card">
            <h4>{row['sentimiento']} {row['titulo']}</h4>
            <p class="fecha">{fecha_str}</p>
            <p>{row['contenido'][:150]}...</p>
            <p class="hashtag">{hashtag}</p>
            <a href="{row['url']}" target="_blank">Leer más</a>
        </div>
    """
    if i % 2 == 0:
        with col1:
            st.markdown(card_html, unsafe_allow_html=True)
    else:
        with col2:
            st.markdown(card_html, unsafe_allow_html=True)

# ---------------------- FOOTER ----------------------
st.sidebar.info("Desarrollado por la Dirección de Planeación, Enlace y Proyectos Estratégicos")
