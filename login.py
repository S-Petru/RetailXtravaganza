import streamlit as st

def app():
    st.subheader('LOGIN PAGE')

    # Stil personalizat pentru formular
    st.markdown("""
    <style>
    div.stTextInput>label, div.stPassword>label {
        color: #ba1414;
    }
    .stTextInput>div>div>input, .stPassword>div>div>input {
        border-color: #ba1414;
    }
    .stButton>button {
        background-color: #ba1414;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Formular de login
    with st.form(key='login_form'):
        username = st.text_input("Nume de utilizator")
        password = st.text_input("Parola", type='password')

        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            # Logica de autentificare (de adăugat aici)
            st.success("Autentificare reușită pentru utilizatorul: " + username)

app()
