import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def train_and_save_model(sales_data):
    sales_data['day_of_week'] = sales_data['Date'].dt.dayofweek
    sales_data['day_of_month'] = sales_data['Date'].dt.day
    sales_data['month'] = sales_data['Date'].dt.month

    X = sales_data[['day_of_week', 'day_of_month', 'month']]
    y = sales_data['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Salveaza modelul antrenat
    joblib.dump(model, 'models/sales_model.joblib')

    # Returneaza media si deviatia standard a vanzarilor
    return y.mean(), y.std()

def get_sales_alerts(some_threshold):
    model = joblib.load('models/sales_model.joblib')

    sales_data = pd.read_excel('data/sales_and_eodStocks.xlsx')
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])
    sales_data['day_of_week'] = sales_data['Date'].dt.dayofweek
    sales_data['day_of_month'] = sales_data['Date'].dt.day
    sales_data['month'] = sales_data['Date'].dt.month
    X_sales = sales_data[['day_of_week', 'day_of_month', 'month']]

    # Fac predictii pe aceste date
    predicted_sales = model.predict(X_sales)

    # Generează alertele
    alerts = []
    for idx, prediction in enumerate(predicted_sales):
        if prediction < some_threshold:
            alert = f"Alertă de scădere a vânzărilor la data {sales_data.iloc[idx]['Date']}: predicție vânzări {prediction}"
            alerts.append(alert)

    return alerts

def calculate_alert_threshold():
    sales_data = pd.read_excel('data/sales_and_eodStocks.xlsx')
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])
    mean_sales, std_sales = train_and_save_model(sales_data)
    return mean_sales - 2 * std_sales

if __name__ == "__main__":
    sales_data = pd.read_excel('data/sales_and_eodStocks.xlsx')
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])

    mean_sales, std_sales = train_and_save_model(sales_data)
    some_threshold = mean_sales - 2 * std_sales

    alerts = get_sales_alerts(some_threshold)
    for alert in alerts:
        print(alert)
