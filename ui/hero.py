import streamlit as st

def render_hero():
    with st.container(horizontal_alignment='center'):
        st.image("assets/logo8.svg", width= 500)

    st.markdown("<h1 style='text-align:center'>Speech intelligence, powered by AI</h2>", unsafe_allow_html=True)
    st.space(70)
    st.markdown("<h5 style='text-align:center; color: black'>Get instant AI-powered feedback on your speaking performance.</h5>", unsafe_allow_html=True)
    st.space(15)