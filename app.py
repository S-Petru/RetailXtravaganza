import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.data_preprocessing import preprocess_sales_data, preprocess_transactions_data
from scripts.sales_prediction import explore_sales_and_stock_data, develop_sales_prediction_models
from scripts.inventory_optimization import develop_inventory_optimization_model
from scripts.recommendation_system import analyze_customer_purchase_behavior, develop_recommendation_system
from scripts.notification_generation import generate_notifications

# Încarcăm datele
sales_data = pd.read_excel('data/sales_and_eodStocks.xlsx')
transactions_data = pd.read_excel('data/transactions.xlsx')

# Aplicăm preprocesarea pentru fiecare set de date
sales_data = preprocess_sales_data(sales_data)
transactions_data = preprocess_transactions_data(transactions_data)

# Exemplu de explorare a datelor și dezvoltare a modelelor
explore_sales_and_stock_data(sales_data, sales_data)
develop_sales_prediction_models(sales_data)

# Exemplu de dezvoltare a modelului de optimizare a stocurilor
inventory_optimization_results = develop_inventory_optimization_model(sales_data)

# Exemplu de analiză a comportamentului de cumpărare și dezvoltare a sistemului de recomandare
analyze_customer_purchase_behavior(transactions_data)
recommendation_results = develop_recommendation_system(transactions_data)

# Exemplu de generare a notificărilor
generate_notifications(inventory_optimization_results, recommendation_results)

# Layout-ul dashboard-ului cu Streamlit
st.title('RetailX Dashboard')

# Afișăm graficul pentru vânzări istorice
st.plotly_chart(px.line(sales_data, x='Date', y='Sales', title='Vânzări istorice'))

# Alte componente sau grafice pot fi adăugate în funcție de necesități
