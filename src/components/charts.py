import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

PALETA_FINANCIAL = ["#28A745", "#FFC107", "#17A2B8", "#6F42C1", "#FD7E14", "#DC3545"]
def render_patrones_gastos(resumen_gastos, ingreso_mensual):
    st.subheader("📌 Patrones de Consumo y Presupuesto")

    df_gastos = pd.DataFrame(list(resumen_gastos.items()), columns=["Categoría", "Monto ($)"])
    df_gastos["Categoría"] = df_gastos["Categoría"].str.capitalize()

    gasto_total = df_gastos["Monto ($)"].sum()

    col_pie, col_budget = st.columns(2)

    with col_pie:
        st.markdown("##### Distribución por Categoría (Modelo NLP)")
        fig_pie = px.pie(
            df_gastos,
            values="Monto ($)",
            names="Categoría",
            hole=0.45,
            color_discrete_sequence=PALETA_FINANCIAL
        )

        fig_pie.update_traces(
            textposition='inside',
            textinfo='percent',
            pull=[0.02] * len(df_gastos), # <--- Despega todas las piezas
            
        )

        fig_pie.update_layout(
            margin=dict(t=20, b=20, l=10, r=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=True
        )
        st.plotly_chart(fig_pie, width="stretch")

    with col_budget:
        st.markdown("##### Presupuesto Consumido vs. Ingreso")
        
        pct_consumido = min((gasto_total / ingreso_mensual) * 100.0 if ingreso_mensual > 0 else 0, 100.0)

        

        fig_bullet = go.Figure(go.Indicator(
            mode="number+gauge",
            value=gasto_total,
            number={'prefix': "$", 'valueformat': ",.2f"},
            title={'text': f"Gasto Total (${gasto_total:,.2f}) / Ingreso (${ingreso_mensual:,.2f})"},
            gauge={
                'shape': "bullet",
                'axis': {'range': [0, ingreso_mensual]},
                'bar': {'color': "#DC3545" if pct_consumido > 80 else "#28A745"},
                'threshold': {
                    'line': {'color': "black", 'width': 2},
                    'thickness': 0.75,
                    'value': ingreso_mensual * 0.8
                }
            }
        ))
        fig_bullet.update_layout(height=180, margin=dict(t=40, b=20, l=20, r=20))
        st.plotly_chart(fig_bullet, width="stretch")
        st.caption(f"💡 Has consumido el **{pct_consumido:.1f}%** de tu ingreso mensual configurado.")

def render_historial_tendencia(historial):
    st.subheader("📉 Evolución Histórica Financiera")
    df_hist = pd.DataFrame(historial)

    if not df_hist.empty:
        fig_line = px.line(
            df_hist,
            x="fecha",
            y="gastoTotal",
            markers=True,
            title="Evolución de Gasto Total Mensual",
            labels={"fecha": "Mes / Diagnóstico", "gastoTotal": "Gasto Total ($)"},
            color_discrete_sequence=["#17A2B8"]
        )
        fig_line.update_layout(margin=dict(t=30, b=20, l=10, r=10))
        st.plotly_chart(fig_line, width="stretch")