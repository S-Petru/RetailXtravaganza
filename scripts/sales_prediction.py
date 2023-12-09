# sales_prediction.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import plotly.express as px

def explore_sales_and_stock_data(sales_data, stock_data):
    """Explorează datele de vânzări și stocuri."""
    # Analiza patternurilor și identificarea variațiilor sezoniere pot fi adăugate aici
    # Poate fi inclus și cod pentru impactul evenimentelor speciale
    # Utilizează Plotly Express pentru a crea vizualizări relevante
    fig = px.line(sales_data, x='Date', y='Sales', title='Vânzări istorice')
    fig.show()

def develop_sales_prediction_models(sales_data):
    """Dezvoltă modele de predicție pentru cerere."""
    # Efectuează preprocesarea datelor pentru modelul de predicție
    sales_data['Date'] = pd.to_numeric(sales_data['Date'])  # Convertirea coloanei 'Date' la tip numeric

    # Separă datele în setul de antrenare și cel de testare
    train_data, test_data = train_test_split(sales_data, test_size=0.2, random_state=42)

    # Selectează caracteristicile pentru antrenare și etichetele
    X_train = train_data[['Date']]
    y_train = train_data['Sales']
    X_test = test_data[['Date']]
    y_test = test_data['Sales']

    # Inițializează și antrenează modelul de regresie liniară
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Efectuează predicții pe setul de testare
    predictions = model.predict(X_test)

    # Calculează și afișează metrici de performanță
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    # Afișează vizualizarea rezultatelor
    fig = px.scatter(test_data, x='Date', y='Sales', title='Rezultate Predicție Vânzări')
    fig.add_trace(px.line(test_data, x='Date', y=predictions, name='Predictions').data[0])
    fig.show()

if __name__ == "__main__":
    # Încarcă datele din fișierul Excel
    sales_data = pd.read_excel('data/sales_and_eodStocks.xlsx')

    # Explorează datele și dezvoltă modelele de predicție
    explore_sales_and_stock_data(sales_data, stock_data)
    develop_sales_prediction_models(sales_data)
