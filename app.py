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
hoy = datetime.now().date()
opciones = {
    "Hoy": hoy,
    "Últimos 7 días": hoy - timedelta(days=7),
    "Últimos 30 días": hoy - timedelta(days=30),
    "Últimos 90 días": hoy - timedelta(days=90),
    "Histórico": None
}
seleccion = st.sidebar.selectbox("Selecciona un periodo:", list(opciones.keys()))

# ➤ Filtrado por temporalidad
if seleccion != "Histórico":
    fecha_min = opciones[seleccion]
    fecha_max = hoy
    df = df[(df["fecha"].dt.date >= fecha_min) & (df["fecha"].dt.date <= fecha_max)]

# ➤ Filtro por pestaña / subpestaña
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

# ➤ Filtro por texto
query = st.sidebar.text_input("🔍 Buscar texto:")
if query:
    df = df[df["texto_completo"].str.contains(query, case=False, na=False)]

# ➤ Mostrar conteo
if not df.empty:
    st.markdown(f"📅 Noticias filtradas: {df['fecha'].min().date()} → {df['fecha'].max().date()}")
    st.markdown(f"🧮 Total de noticias mostradas: {len(df)}")
else:
    st.warning("No hay noticias que coincidan con los filtros seleccionados.")

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
    flex: 0 0 auto;
    width: 280px;
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
    with col1 if i % 2 == 0 else col2:
        st.markdown(card_html, unsafe_allow_html=True)

# ---------------------- GRÁFICAS ----------------------
st.subheader("📊 Análisis de Sentimientos")

if seleccion in ["Últimos 90 días", "Histórico"]:
    st.markdown("#### Sentimiento diario")
    diario = df.groupby(["fecha", "sentimiento"]).size().unstack(fill_value=0).sort_index()
    if not diario.empty:
        fig1, ax1 = plt.subplots(figsize=(7.5, 3.5))
        for emoji in ["🔴", "🟡", "🟢"]:
            if emoji in diario.columns:
                ax1.plot(diario.index, diario[emoji], label=TRADUCIR_SENTIMIENTO[emoji], color=COLORES_LINEAS[emoji])
        ax1.set_ylabel("Número de Noticias")
        ax1.legend(title="Sentimiento", fontsize=9)
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.tick_params(axis='x', labelrotation=45, labelsize=8)
        st.pyplot(fig1)
    else:
        st.info("No hay datos de sentimiento para este periodo.")

    st.markdown("#### Emociones diarias")
    if set(EMOCIONES).issubset(df.columns):
        emociones_df = df[["fecha"] + EMOCIONES].dropna(subset=EMOCIONES, how="all")
        diario_emociones = emociones_df.groupby("fecha")[EMOCIONES].mean().sort_index()
        if not diario_emociones.empty:
            fig3, ax3 = plt.subplots(figsize=(8, 3.5))
            for i, emocion in enumerate(EMOCIONES):
                if emocion in diario_emociones.columns:
                    etiqueta = TRADUCIR_EMOCIONES.get(emocion, emocion)
                    ax3.plot(diario_emociones.index, diario_emociones[emocion], label=etiqueta, color=PALETA_COLORES[i])
            ax3.legend(title="Emoción", fontsize=9)
            ax3.set_ylabel("Nivel Promedio")
            ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            ax3.tick_params(axis='x', labelrotation=45, labelsize=8)
            st.pyplot(fig3)
        else:
            st.info("No hay datos de emociones para este periodo.")
else:
    col1, col2 = st.columns(2)

    with col1:
        conteos = df["sentimiento"].value_counts()
        etiquetas = [TRADUCIR_SENTIMIENTO.get(k, k) for k in ["🔴", "🟡", "🟢"]]
        valores = [conteos.get(k, 0) for k in ["🔴", "🟡", "🟢"]]
        colores = [COLORES_LINEAS[k] for k in ["🔴", "🟡", "🟢"]]
        if sum(valores) > 0:
            fig, ax = plt.subplots(figsize=(3.5, 3.2))
            ax.pie(valores, labels=etiquetas, autopct="%1.1f%%", colors=colores, startangle=90, textprops={'fontsize': 9})
            ax.set_title("Sentimiento Global", fontsize=11)
            st.pyplot(fig)
        else:
            st.info("No hay datos de sentimiento para este periodo.")

    with col2:
        prom = {e: df[e].mean() for e in EMOCIONES if e in df.columns}
        if prom:
            etiquetas_es = [TRADUCIR_EMOCIONES.get(e, e) for e in prom.keys()]
            fig2, ax2 = plt.subplots(figsize=(5.5, 3))
            ax2.bar(etiquetas_es, prom.values(), color=PALETA_COLORES[:len(prom)])
            ax2.set_title("Promedio de Emociones", fontsize=11)
            ax2.set_ylabel("Nivel Promedio", fontsize=9)
            ax2.set_xlabel("Emoción", fontsize=9)
            ax2.tick_params(axis='x', labelsize=9)
            ax2.tick_params(axis='y', labelsize=8)
            st.pyplot(fig2)
        else:
            st.info("No hay datos de emociones para este periodo.")

# ---------------------- FOOTER ----------------------
st.sidebar.info("Desarrollado por la Dirección de Planeación, Enlace y Proyectos Estratégicos")

#------
st.markdown("### 🔍 Diagnóstico de noticias después del 12/03/2025")

diagnostico = df[df["fecha"] > pd.to_datetime("2025-03-12")]
st.write(f"📰 Noticias después del 12/03/2025: {len(diagnostico)}")

st.write("📊 Conteo por pestaña:")
st.write(diagnostico["pestaña"].value_counts(dropna=False))

st.write("📊 Conteo por subpestaña:")
if "subpestaña" in diagnostico.columns:
    st.write(diagnostico["subpestaña"].value_counts(dropna=False))

