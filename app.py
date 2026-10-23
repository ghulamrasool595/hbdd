import streamlit as st
import streamlit.components.v1 as components

# This removes Streamlit's default margins so the app looks like a phone screen
st.set_page_config(layout="centered")

# Open and read your custom HTML file
with open("index.html", "r", encoding="utf-8") as file:
    custom_html = file.read()

# Embed the HTML into your Streamlit app
components.html(custom_html, height=850, scrolling=False)