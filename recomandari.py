import streamlit as st
import pandas as pd
import sys

sys.path.insert(1, './scripts/') 
import recommendation_system

def app():
    st.title('Top 10 Recomandări de Reaprovizionare a Stocurilor')

    # Încărcarea datelor
    transactions_data = pd.read_excel('data/transactions.xlsx')

    # Crearea unui buton pentru generarea top 10 produse recomandate pentru reaprovizionare
    if st.button('Afișează Top 10 Recomandări de Reaprovizionare'):
        top_products_by_volume = recommendation_system.get_top_products_by_volume(transactions_data)
        
        if top_products_by_volume.empty:
            st.error('Nu există suficiente date pentru a genera top 10 recomandări.')
        else:
            # Afișați top 10 produse recomandate pentru reaprovizionare
            st.subheader('Top 10 Recomandări de Reaprovizionare a Stocurilor:')
            st.table(top_products_by_volume)


# Asigurați-vă că apelul funcției app() este executat doar atunci când acest script este rulat direct
if __name__ == '__main__':
    app()