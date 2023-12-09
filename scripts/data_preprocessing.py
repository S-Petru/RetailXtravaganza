import pandas as pd

def load_data(file_path):
    """Încarcă datele din fișierul Excel și returnează un DataFrame."""
    return pd.read_excel(file_path)

def preprocess_sales_data(sales_data):
    """Efectuează preprocesarea datelor de vânzări."""
    # Converteste coloana 'Date' la tipul de dată
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])

    # Alte preprocesări pot fi adăugate aici, în funcție de necesități

    return sales_data

def preprocess_transactions_data(transactions_data):
    """Efectuează preprocesarea datelor de tranzacții."""
    # Converteste coloana 'Date' la tipul de dată
    transactions_data['Date'] = pd.to_datetime(transactions_data['Date'])

    # Alte preprocesări pot fi adăugate aici, în funcție de necesități

    return transactions_data

def main():
    # Încarcă datele din fișierele Excel
    sales_data = load_data('data/sales_and_eodStocks.xlsx')
    transactions_data = load_data('data/transactions.xlsx')

    # Aplică preprocesarea pentru fiecare set de date
    sales_data = preprocess_sales_data(sales_data)
    transactions_data = preprocess_transactions_data(transactions_data)

    # Salvează seturile de date preprocesate (opțional)
    sales_data.to_csv('data/sales_preprocessed.csv', index=False)
    transactions_data.to_csv('data/transactions_preprocessed.csv', index=False)

# Nu este necesar să ai o funcție 'run()' aici

if __name__ == "__main__":
    main()