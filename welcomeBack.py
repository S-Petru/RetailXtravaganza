import streamlit as st

# Setarea configurației paginii
# st.set_page_config(page_title='Welcome to RetailX', layout='wide')

# Funcția pentru pagina de întâmpinare
def app():
    # Crearea unui layout cu coloane
    col1, col2 = st.columns([1, 2])

    # Col1: Imagine sau Logo-ul companiei
    with col1:
        st.image('logo.png', width=200)  # Asigurați-vă că înlocuiți cu calea corectă a imaginii

    # Col2: Mesaj de întâmpinare
    with col2:
        st.write("# Welcome to RetailX")
        st.write("### Your one-stop destination for all retail analytics.")
        st.write("Navigate through our application to explore various metrics, trends, "
                 "and alerts that are essential for your retail operations.")
        st.markdown("#### How to get started:")
        st.markdown("""
        - **Login** to access your personalized dashboard.
        - Explore the **Trending** section to see what's hot in the market right now.
        - Check the **Alerts** for any immediate updates or actions required.
        - Utilize the **Explore Metrics** for a deep dive into your data.
        - Contact us anytime through the **Support** section for assistance.
        """)

# Rularea paginii de întâmpinare
app()
