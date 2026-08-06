import streamlit as st
from src.services.api_client import (
    obtener_analisis_predict,
    obtener_historial_usuario,
    obtener_transacciones_detalle
)
from src.components.kpis import render_kpis
from src.components.charts import render_patrones_gastos, render_historial_tendencia
from src.components.recommendations import render_recomendaciones
from src.components.transactions import render_tabla_transacciones

# 1. Configuración de página
st.set_page_config(
    page_title="FinanceAI - Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 FinanceAI — Control Financiero Inteligente")
st.caption("Dashboard Conectado con Backend Spring Boot & ML (OpenAPI Mapped)")
st.markdown("---")

# 2. Carga de datos desde los microservicios
data_predict = obtener_analisis_predict()
historial_data = obtener_historial_usuario()
transacciones_data = obtener_transacciones_detalle()

# 3. CAPA 1: KPIs y Diagnóstico
render_kpis(data_predict)
st.markdown("---")

# 4. CAPA 2: Patrones de Consumo (Dona + Bullet de Presupuesto)
resumen_gastos = data_predict.get("resumenGastos", {})
ingreso_mensual = float(data_predict.get("ingreso_mensual", 4500.0))
render_patrones_gastos(resumen_gastos, ingreso_mensual)
st.markdown("---")

# 5. CAPA 3: Evolución Histórica
render_historial_tendencia(historial_data)
st.markdown("---")

# 6. CAPA 4: Insights de IA y Tabla Detallada
render_recomendaciones(data_predict.get("recomendaciones", []))
st.markdown("---")
render_tabla_transacciones(transacciones_data)