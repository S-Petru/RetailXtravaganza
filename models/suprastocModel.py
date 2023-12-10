import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def suprastocModel(sales_data_path, transactions_data_path, sample_size=10000):
    # Încărcarea datelor cu tipuri de date optimizate
    dtype_dict = {'Product_ID': 'category', 'Sales': 'float32', 'Revenue': 'float32', 'EndOfDayStock': 'int32'}
    sales_data = pd.read_csv(sales_data_path, usecols=['Product_ID', 'Sales', 'Revenue', 'EndOfDayStock'], dtype=dtype_dict)
    transactions_data = pd.read_csv(transactions_data_path, usecols=['Product_ID', 'Description'], dtype={'Product_ID': 'category', 'Description': 'category'})
   
    # Eșantionarea unui subset de date
    sales_data_sample = sales_data.sample(n=sample_size, random_state=42)

    # Calculul vânzărilor medii pe produs
    mean_sales = sales_data_sample.groupby('Product_ID')['Sales'].mean().reset_index()

    # Combinarea datelor de vânzări cu media vânzărilor
    combined_data = pd.merge(sales_data_sample, mean_sales, on='Product_ID', suffixes=('', '_mean'))

    # Calculul unui indicator de suprastoc
    # De exemplu, presupunem că un produs este în suprastoc dacă 'EndOfDayStock' depășește de 5 ori vânzările medii
    combined_data['IsOverstock'] = combined_data['EndOfDayStock'] > 5 * combined_data['Sales_mean']

    # Selectarea caracteristicilor pentru model
    X = combined_data[['Sales', 'Revenue', 'EndOfDayStock']]
    y = combined_data['IsOverstock']

    combined_data.set_index('Product_ID', inplace=True)

    # Împărțirea datelor în seturi de antrenament și testare
    X_train, X_test, y_train, y_test = train_test_split(combined_data[['Sales', 'Revenue', 'EndOfDayStock']], combined_data['IsOverstock'], test_size=0.2, random_state=42)

    # Crearea și antrenarea modelului
    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(X_train, y_train)

    # Predicții pe setul de test
    predictions = model.predict(X_test)
    X_test['PredictedOverstock'] = predictions
    X_test.reset_index(inplace=True)

    # Returnarea rezultatelor
    results = X_test[['Product_ID', 'PredictedOverstock']]
    return results