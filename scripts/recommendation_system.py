import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def analyze_customer_purchase_behavior(transactions_data):
    """Analizează comportamentul de cumpărare al clienților."""
    # Se creează un tabel de apariție a elementelor
    basket = (transactions_data.groupby(['Invoice', 'Description'])['Quantity']
              .sum().unstack().reset_index().fillna(0)
              .set_index('Invoice'))

    # Transformă valorile în binare (0 sau 1) pentru a reflecta dacă produsul a fost cumpărat sau nu
    basket_sets = basket.applymap(lambda x: 1 if x > 0 else 0)

    # Exclud produsele care apar rar
    product_frequency = basket_sets.sum(axis=0)
    basket_sets = basket_sets.loc[:, product_frequency > basket_sets.shape[0] * 0.01]

    # Aplică algoritmul Apriori pentru a identifica itemset-urile frecvente
    frequent_itemsets = apriori(basket_sets, min_support=0.01, use_colnames=True)

    # Aplică regulile de asociație pentru a genera recomandări
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    # Afișează regulile de asociație
    print(rules)

def develop_recommendation_system(transactions_data, customer_id):
    """Dezvoltă un sistem de recomandare personalizat pentru clienți."""
    # Filtrare tranzacții pentru clientul specificat
    customer_transactions = transactions_data[transactions_data['Customer ID'] == customer_id]

    # Identifică produsele pe care le-a cumpărat
    purchased_products = set(customer_transactions['Description'])

    # Dezvoltă recomandări pe baza produselor cumpărate anterior de către client
    recommendations = recommend_products(purchased_products, transactions_data)

    # Afișează recomandările
    print(f"Recomandări pentru clientul {customer_id}: {recommendations}")

def recommend_products(purchased_products, transactions_data):
    """Generează recomandări bazate pe produsele cumpărate anterior."""
    # Se creează un tabel de apariție a elementelor
    basket = (transactions_data.groupby(['Invoice', 'Description'])['Quantity']
              .sum().unstack().reset_index().fillna(0)
              .set_index('Invoice'))

    # Transformă valorile în binare (0 sau 1) pentru a reflecta dacă produsul a fost cumpărat sau nu
    basket_sets = basket.applymap(lambda x: 1 if x > 0 else 0)

    # Exclud produsele care apar rar
    basket_sets = basket_sets.loc[:, basket_sets.sum() > basket_sets.shape[0] * 0.01]  # De exemplu, exclude produsele care apar în mai puțin de 1% din facturi

    # Aplică algoritmul Apriori cu un min_support mai mare
    frequent_itemsets = apriori(basket_sets, min_support=0.02, use_colnames=True)  # Crește min_support pentru a reduce numărul de itemset-uri

    # Aplică regulile de asociație pentru a genera recomandări
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    # Filtrare reguli pentru a exclude cele care conțin produse deja cumpărate
    recommendations = rules[~rules['antecedents'].apply(lambda x: any(product in purchased_products for product in x))]
    
    return recommendations

def get_replenishment_recommendations(transactions_data):
    """Returnează top 10 produse care necesită reaprovizionare."""
    # Calculăm suma totală vândută pentru fiecare produs
    sales_totals = transactions_data.groupby('Description')['Quantity'].sum()

    # Sortăm produsele în funcție de cantitatea totală vândută în ordine descrescătoare
    top_products = sales_totals.sort_values(ascending=False).head(10)

    return top_products
