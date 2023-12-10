import streamlit as st
import pandas as pd
import sys

sys.path.insert(1, './scripts/') 
from models.suprastocModel import suprastocModel

def app():
    st.header('Alerte de Stoc')

    if st.button('Verifică Suprastocul'):
        suprastoc_results = suprastocModel('data/sales_and_eodStocks.csv', 'data/transactions.csv')
        top_overstock_products = suprastoc_results.head(10)  # Afișarea primelor 10 rânduri

        if not top_overstock_products.empty:
            st.subheader('Top 10 Produse în Suprastoc:')
            st.dataframe(top_overstock_products)
        else:
            st.write('Niciun produs nu necesită ajustări de stoc în acest moment.')

if __name__ == '__main__':
    app()
