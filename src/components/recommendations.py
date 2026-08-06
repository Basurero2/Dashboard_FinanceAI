import streamlit as st

def render_recomendaciones(recomendaciones):
    st.subheader("💡 Recomendaciones de la Inteligencia Artificial")
    if recomendaciones:
        for rec in recomendaciones:
            st.info(f"🤖 **Sugerencia:** {rec}")
    else:
        st.success("🟢 Tu comportamiento financiero es óptimo. Mantén tus hábitos actuales.")