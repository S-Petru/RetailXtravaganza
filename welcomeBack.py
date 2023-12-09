import streamlit as st

def app():
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image('logo.png', width=225)  # Adjust the path and size as needed

    with col2:
        st.markdown("# Bun venit la Dashboard-ul <span style='color: #ba1414;'>RetailX Analytics</span>!", unsafe_allow_html=True)
        st.markdown("### Explorare, analiză și insight-uri valoroase.", unsafe_allow_html=True)

    st.markdown("""
    #### Descoperă funcționalitățile:
    - **Login** pentru acces la tabloul tău de bord personalizat.
    - Explorează secțiunea <span style='color: #ba1414;'>**Trending**</span> pentru a vedea ultimele tendințe din piață.
    - Verifică secțiunea <span style='color: #ba1414;'>**Alerte**</span> pentru actualizări importante și acțiuni necesare.
    - Folosește <span style='color: #ba1414;'>**Explore Metrics**</span> pentru o analiză detaliată a datelor tale.
    - Contactează-ne oricând prin secțiunea <span style='color: #ba1414;'>**Suport**</span> pentru asistență.
    """ , unsafe_allow_html=True)
    st.write("#### Găsește rapid informațiile de care ai nevoie:")
    st.write("Folosind acest dashboard, vei putea accesa rapid <span style='color: #ba1414;'>statistici actualizate</span>, "
             "urmări <span style='color: #ba1414;'>alerte importante</span> și obține insight-uri care te vor ajuta în luarea deciziilor strategice. "
             "Interfața noastră ușor de folosit îți permite să navighezi eficient între diferite secțiuni, "
             "maximizând productivitatea ta.", unsafe_allow_html=True)

app()
