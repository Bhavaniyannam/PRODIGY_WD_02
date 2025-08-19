import streamlit as st

st.set_page_config(page_title="Stopclock", layout="centered")
st.title("⏱️ Stopclock")
st.write("A simple stopwatch built with HTML, CSS, and JavaScript.")

with open("stopclock.html", "r", encoding="utf-8") as f:
    html_data = f.read()

st.components.v1.html(html_data, height=600)
