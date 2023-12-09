import streamlit as st

def app():
    st.subheader('Pagina de Suport')

    # Stilizarea paginii
    st.markdown("""
    <style>
    .info-box {
        padding: 10px;
        border: 2px solid #ba1414;
        border-radius: 5px;
        margin: 10px 0px;
    }
    .info-title {
        color: #ba1414;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #ba1414;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Informații utile
    # (Codul pentru cutiile de informații)

    # Formular pentru trimiterea unui ticket de suport
    st.markdown("### Trimite un Ticket de Suport")
    with st.form(key='support_ticket'):
        name = st.text_input("Numele tău")
        email = st.text_input("Email")
        issue = st.text_area("Descrie problema")
        submit_button = st.form_submit_button(label='Trimite Ticket')

        if submit_button:
            st.success(f"Ticketul a fost trimis cu succes! Vom reveni cu un răspuns la adresa {email}.")

app()
