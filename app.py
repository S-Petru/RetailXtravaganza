import streamlit as st
from streamlit_option_menu import option_menu
import welcomeBack, login, alerts, recomandari, anomalii

st.set_page_config(
        page_title="Explore Metrics",
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
                menu_title='Explore Metrics',
                options=['Bine Ai Venit', 'Login','Recomandari','Alerte', 'Anomalii Stoc'],
                icons=['emoji-laughing','person-circle','graph-up-arrow', 'exclamation-triangle', 'database-exclamation'],
                menu_icon='clipboard-data',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'#354649'},
                    "icon": {"color": "white", "font-size": "24px"}, 
                    "nav-link": {"color":"white","font-size": "18px", "text-align": "left", "margin":"8px 0px", "--hover-color": "#6C7A89"},
                    "nav-link-selected": {"background-color": "#A3C6C4"}}
                
                )

        if app == "Bine Ai Venit":
            welcomeBack.app()  
        if app == "Login":
            login.app()  
        if app == "Recomandari":
            recomandari.app()        
        if app == 'Alerte':
            alerts.app()  
        if app == "Anomalii Stoc":
            anomalii.app()  
             
    run()            
      