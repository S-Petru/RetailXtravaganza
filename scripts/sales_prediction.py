import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import plotly.express as px

def explore_sales_and_stock_data(sales_data):
    """Explorează datele de vânzări."""
    # Vizualizează datele de vânzări
    fig = px.line(sales_data, x='Date', y='Sales', title='Vânzări istorice')
    fig.show()

def develop_sales_prediction_models(sales_data):
    """Dezvoltă modele de predicție pentru cerere."""
    # Crearea unor caracteristici temporale suplimentare pentru model
    sales_data['day_of_week'] = sales_data['Date'].dt.dayofweek
    sales_data['day_of_month'] = sales_data['Date'].dt.day
    sales_data['month'] = sales_data['Date'].dt.month

    # Separă datele în setul de antrenare și cel de testare
    X = sales_data[['day_of_week', 'day_of_month', 'month']]
    y = sales_data['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inițializează și antrenează modelul de regresie liniară
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Efectuează predicții pe setul de testare
    predictions = model.predict(X_test)

    # Calculează și afișează metrici de performanță
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    # Salvează modelul antrenat
    joblib.dump(model, 'models/sales_model.joblib')

if __name__ == "__main__":
    # Încarcă datele din fișierul Excel
    sales_data = pd.read_excel('data/sales_and_eodStocks.xlsx', usecols=['Date', 'Sales'])

    # Asigură-te că 'Date' este în format datetime
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])

    # Explorează datele și dezvoltă modelele de predicție
    explore_sales_and_stock_data(sales_data)
    develop_sales_prediction_models(sales_data)
