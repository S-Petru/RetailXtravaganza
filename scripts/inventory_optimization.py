import pandas as pd
from scipy.optimize import minimize

def develop_inventory_optimization_model(stock_data):
    """Dezvoltă un model simplu de optimizare a stocurilor."""
    # Asumăm că avem costuri constante de depozitare și că vrem să minimizăm aceste costuri

    # Definim funcția obiectiv pentru minimizarea costurilor
    def objective(x):
        return sum(x * stock_data['EndOfDayStock'])

    # Construim constrângerile: stocurile nu pot fi negative
    constraints = ({'type': 'ineq', 'fun': lambda x: x})

    # Inițializăm valori aleatorii pentru stocuri
    initial_stock = [0] * len(stock_data)

    # Aplicăm funcția de minimizare
    result = minimize(objective, initial_stock, constraints=constraints)

    # Salvăm rezultatele
    optimized_stock = result.x

    # Alte acțiuni pot fi adăugate aici în funcție de necesități

    # Salvăm stocurile optimizate într-un fișier sau le returnăm
    stock_data['OptimizedStock'] = optimized_stock
    stock_data.to_csv('data/optimized_stock.csv', index=False)

if __name__ == "__main__":
    # Încarcă datele din fișierul Excel
    stock_data = pd.read_excel('data/sales_and_eodStocks.xlsx')

    # Dezvoltă modelul de optimizare a stocurilor
    develop_inventory_optimization_model(stock_data)
