import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.services.api_client import obtener_analisis_financiero

# 1. Configuración de página
st.set_page_config(
    page_title="FinanceAI - Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 FinanceAI — Salud Financiera Inteligente")
st.caption("Dashboard Conectado con Backend Spring Boot & ML")
st.markdown("---")

# 2. Cargar datos
data = obtener_analisis_financiero()

# 3. EXTRAER Y PARSEAR VARIABLES REALES
perfil = data.get("perfilFinanciero", "RIESGOSO").upper()
prob_modelo = data.get("probabilidad", "0%")

# Convertir el string de nivel_endeudamiento (ej. "12.4%") a número flotante
raw_end = data.get("nivel_endeudamiento", "0%").replace("%", "").strip()
try:
    val_endeudamiento = float(raw_end)
except ValueError:
    val_endeudamiento = 0.0

# Asignar color al perfil
badge_color = "🔴" if perfil == "RIESGOSO" else ("🟡" if perfil in ["EN OBSERVACION", "OBSERVACION"] else "🟢")

# --- BLOQUE 1: KPIs Y VELOCÍMETRO DE ENDEUDAMIENTO ---
st.subheader("📊 Diagnóstico de Salud Financiera")

col_kpi, col_gauge = st.columns([2, 1])

with col_kpi:
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    col1.metric(label="Perfil Diagnosticado (IA)", value=f"{badge_color} {perfil}")
    col2.metric(label="Confianza de Predicción ML", value=prob_modelo)
    col3.metric(label="Nivel de Endeudamiento", value=f"{val_endeudamiento}%")
    col4.metric(label="Capacidad de Ahorro", value=data.get("porcentaje_ahorro", "N/A"))

with col_gauge:
    # VELOCÍMETRO FINANCIERO REAL: Mide Nivel de Endeudamiento (0% a 100%)
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=val_endeudamiento,
        number={'suffix': "%"},
        title={'text': "Nivel de Endeudamiento Real"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#DC3545" if val_endeudamiento > 60 else ("#FFC107" if val_endeudamiento > 30 else "#28A745")},
            'steps': [
                {'range': [0, 30], 'color': "#D4EDDA"},    # 0-30%: Saludable (Verde)
                {'range': [30, 60], 'color': "#FFF3CD"},   # 30-60%: Precaución (Amarillo)
                {'range': [60, 100], 'color': "#F8D7DA"}   # 60-100%: Alto Riesgo (Rojo)
            ]
        }
    ))
    fig_gauge.update_layout(height=190, margin=dict(t=40, b=10, l=20, r=20))
    st.plotly_chart(fig_gauge, width="stretch")

st.markdown("---")

# --- BLOQUE 2: RECOMENDACIONES DE LA IA ---
st.subheader("💡 Recomendaciones Personalizadas")
for rec in data.get("recomendaciones", []):
    st.info(rec)

st.markdown("---")

# --- BLOQUE 3: ANÁLISIS DE GASTOS Y TRANSACCIONES ---
st.subheader("📌 Patrones de Consumo")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("##### Gastos por Categoría (Clasificados por NLP)")
    gastos_dict = data.get("resumenGastos", {})
    df_gastos = pd.DataFrame(list(gastos_dict.items()), columns=["Categoría", "Monto ($)"])
    df_gastos["Categoría"] = df_gastos["Categoría"].str.capitalize()

    fig_pie = px.pie(
        df_gastos,
        values="Monto ($)",
        names="Categoría",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_pie.update_layout(margin=dict(t=20, b=20, l=10, r=10))
    st.plotly_chart(fig_pie, width="stretch")

with col_right:
    st.markdown("##### Distribución por Medio de Pago")
    medios_dict = data.get("gastosPorMedioPago", {})
    df_medios = pd.DataFrame(list(medios_dict.items()), columns=["Medio de Pago", "Monto ($)"])

    fig_bar = px.bar(
        df_medios,
        x="Medio de Pago",
        y="Monto ($)",
        color="Medio de Pago",
        text_auto='.2f',
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_bar.update_layout(showlegend=False, margin=dict(t=20, b=20, l=10, r=10))
    st.plotly_chart(fig_bar, width="stretch")

st.markdown("---")

# --- BLOQUE 4: TABLA DETALLADA ---
with st.expander("🔍 Ver desglose de datos en formato tabla"):
    st.dataframe(df_gastos, width="stretch")