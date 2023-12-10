import streamlit as st
import pandas as pd
from twilio.rest import Client
import sys

sys.path.insert(1, './scripts/') 
from models.suprastocModel import suprastocModel

# Credențialele Twilio
twilio_account_sid = 'AC27d3477d4e895930aea02481e6cb0b07'
twilio_auth_token = 'c53275331abe97aa56ab265d4672b029'
twilio_phone_number = '+13107361968'
destination_phone_number = '+40723290926'

def app():
    st.header('Alerte de Stoc')

    # Adăugați un argument `key` unic pentru checkbox
    if st.checkbox('Verifică Suprastocul și Trimite Alertă', key='unique_key_for_check_overstock'):
        suprastoc_results = suprastocModel('data/sales_and_eodStocks.csv', 'data/transactions.csv')
        first_overstock_product = suprastoc_results.head(1)
        product_id = first_overstock_product['Product_ID'].iloc[0]
        is_overstocked = first_overstock_product['PredictedOverstock'].iloc[0]

        if is_overstocked:
            # Crearea mesajului
            message_content = f"Dragă Manager de Stoc,\n\nBazându-ne pe ultimele analize, vă sugerăm să ajustați stocul pentru Produsul cu ID-ul {product_id}. Recomandăm o creștere sau scădere corespunzătoare a stocului, având în vedere tendințele de creștere sau scădere ale cererii. Detalii complete ale recomandării pot fi găsite în dashboard-ul nostru de management al stocurilor.\n\nCu respect,\nEchipa de Management a Stocurilor"

            # Trimiterea mesajului SMS folosind Twilio
            twilio_client = Client(twilio_account_sid, twilio_auth_token)
            twilio_client.messages.create(body=message_content, from_=twilio_phone_number, to=destination_phone_number)

            st.success('Mesajul a fost trimis!')
        else:
            st.write('Niciun produs nu necesită ajustări de stoc în acest moment.')

# Asigurați-vă că apelul funcției app() este executat doar atunci când acest script este rulat direct
if __name__ == '__main__':
    app()
