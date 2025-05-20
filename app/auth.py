import streamlit as st

def login():
    st.sidebar.title("🔐 Авторизация")
    password = st.sidebar.text_input("Введите пароль", type="password")
    if password != "admin123":
        st.warning("Неверный пароль!")
        st.stop()
