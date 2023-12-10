import streamlit as st
from models.suprastocModel import suprastocModel

def app():
    st.subheader('Pagina de Alerte')

    if st.button("Rulează Modelul de Suprastoc"):
        results = suprastocModel('data/sales_and_eodStocks.csv', 'data/transactions.csv')

        if results is not None and not results.empty:
            st.write("Produse estimate ca fiind în suprastoc:")
            st.dataframe(results)
        else:
            st.write("Nu există date disponibile pentru a estima suprastocul.")
    else:
        st.text("Apasă butonul pentru a rula modelul.")

app()
