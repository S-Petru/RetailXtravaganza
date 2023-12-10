# notification_generation.py
import pandas as pd

def generate_notifications(inventory_optimization_results, recommendation_results):
    """Generează notificări folosind rezultatele optimizării stocurilor și recomandărilor."""
    # Preluarea detaliilor relevante din rezultatele optimizării stocurilor
    low_stock_products = inventory_optimization_results[inventory_optimization_results['Stock Level'] == 'Low']['Product']

    # Preluarea produselor recomandate
    recommended_products = recommendation_results['Product'].tolist()

    # Generarea notificărilor
    notifications = []

    for product in low_stock_products:
        if product in recommended_products:
            notification = f"Produsul {product} are un nivel scăzut de stoc. Recomandare: consultați recomandările pentru acest produs."
        else:
            notification = f"Atenție! Nivelul de stoc pentru produsul {product} este scăzut."

        notifications.append(notification)

    # Afișarea notificărilor
    for notification in notifications:
        print(notification)

if __name__ == "__main__":
    # Încarcă rezultatele optimizării stocurilor și recomandările
    inventory_optimization_results = pd.read_csv('path_to_inventory_optimization_results.csv')
    recommendation_results = pd.read_csv('path_to_recommendation_results.csv')

    # Generează notificările
    generate_notifications(inventory_optimization_results, recommendation_results)
