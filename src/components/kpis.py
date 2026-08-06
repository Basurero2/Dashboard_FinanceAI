import streamlit as st
import plotly.graph_objects as go

def render_kpis(data):
    st.subheader("📊 Diagnóstico y Métricas Principales")

    perfil = str(data.get("perfilFinanciero", "RIESGOSO")).upper().replace("_", " ")
    prob = float(data.get("probabilidad", 0.0)) * 100.0
    val_end = float(data.get("nivel_endeudamiento", 0.0))
    frec_ahorro = data.get("frecuencia_ahorro", "N/A")

    badge_color = "🔴" if "RIESGOSO" in perfil else ("🟡" if "OBSERVACION" in perfil else "🟢")

    col_kpi, col_gauge = st.columns([2, 1])

    with col_kpi:
        c1, c2 = st.columns(2)
        c3, c4 = st.columns(2)

        c1.metric(label="Perfil Diagnóstico IA", value=f"{badge_color} {perfil}")
        c2.metric(label="Certeza de Predicción ML", value=f"{prob:.1f}%")
        c3.metric(label="Nivel de Endeudamiento", value=f"{val_end}%")
        c4.metric(label="Frecuencia de Ahorro", value=frec_ahorro)

    with col_gauge:
        color_riesgo = "#DC3545" if val_end > 60 else ("#FFC107" if val_end > 30 else "#28A745")
        
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=val_end,
            number={'suffix': "%"}, 
            title={'text': "Uso de Línea de Crédito"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': color_riesgo}, 
                # CLAVE AQUÍ: Usar opacidad (15% de blanco/gris). 
                # En fondo negro se ve gris oscuro (#222), en fondo blanco se ve gris muy claro (#eee)
                'bgcolor': "rgba(128, 128, 128, 0.15)", 
                'borderwidth': 0
            }
        ))
        
        fig_gauge.update_layout(
            height=210, 
            margin=dict(t=50, b=10, l=20, r=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_gauge, use_container_width=True)