import streamlit as st
from streamlit_option_menu import option_menu
import welcomeBack, alerts, recomandari, anomalii, suport

st.set_page_config(
        page_title="RetailX",
        page_icon="favicon.ico",
)
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='RetailX Metrics',
                options=['Bine Ai Venit', 'Anomalii Stoc', 'Recomandari', 'Alerte', 'Suport'],
                icons=['emoji-laughing', 'database-exclamation', 'graph-up-arrow', 'exclamation-triangle', 'headset'],
                menu_icon='clipboard-data',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'#0E1117'},
                    "icon": {"color": "white", "font-size": "32px"}, 
                    "nav-link": {"color":"white","font-size": "18px", "text-align": "left", "margin":"8px 0px", "--hover-color": "#6C7A89"},
                    "nav-link-selected": {"color":"#ba1414", "background-color": "white", "font-size": "22px"}}
                )

        if app == "Bine Ai Venit":
            welcomeBack.app()
        if app == "Recomandari":
            recomandari.app()        
        if app == 'Alerte':
            alerts.app()  
        if app == "Anomalii Stoc":
            anomalii.app()  
        if app == "Suport":
            suport.app()  

        # Afiseaza copyright-ul în partea de jos a sidebar-ului
        st.sidebar.markdown("---")
        st.sidebar.markdown("© 2023 DevMinds")

    run()            
      