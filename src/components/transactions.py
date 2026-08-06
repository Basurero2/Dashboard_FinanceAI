import streamlit as st
import pandas as pd

def render_tabla_transacciones(transacciones):
    with st.expander("🔍 Historial de Transacciones Registradas (`/api/v1/transactions`)", expanded=False):
        df_tx = pd.DataFrame(transacciones)
        
        if not df_tx.empty:
            # Filtro por categoría o búsqueda
            col_search, _ = st.columns([2, 2])
            with col_search:
                filtro = st.text_input("Filtrar por descripción o categoría:", "")

            if filtro:
                df_tx = df_tx[
                    df_tx["descripcion"].str.contains(filtro, case=False, na=False) |
                    df_tx["categoria"].str.contains(filtro, case=False, na=False)
                ]

            st.dataframe(df_tx, width="stretch")
        else:
            st.write("No hay transacciones registradas.")