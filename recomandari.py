import streamlit as st
import plotly.express as px
import pandas as pd
import sys

sys.path.insert(1, './scripts/') 
import recommendation_system

def app():
    st.header('Top 10 Produse care Necesită Reaprovizionare')

    # Crearea unui buton pentru generarea top 10 produse care necesită reaprovizionare
    if st.button('Afișează Top 10 Produse pentru Reaprovizionare'):
        # Încărcarea datelor de tranzacții
        transactions_data = pd.read_excel('data/transactions.xlsx')

        top_products = recommendation_system.get_replenishment_recommendations(transactions_data)

        # Verificăm dacă există produse pentru reaprovizionare
        if not top_products.empty:
            st.subheader('Top 10 Produse pentru Reaprovizionare:')
            # Construim un string formatat cu bullet points
            products_list = "\n".join([f"- {product}: {total} unități vândute" for product, total in top_products.items()])
            st.markdown(products_list)

            # Crearea DataFrame-ului pentru diagrama Plotly
            df_top_products = pd.DataFrame(top_products).reset_index()
            df_top_products.columns = ['Descriere Produs', 'Cantitate Vândută']

            # Crearea unei diagrame Plotly
            fig = px.bar(df_top_products, x='Descriere Produs', y='Cantitate Vândută', title='Top 10 Produse pentru Reaprovizionare')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Nu există suficiente date pentru generarea top 10 produse.")