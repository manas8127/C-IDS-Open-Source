import app1
import app2
import app3
import app4
from cyber_mads import *
import streamlit as st
import streamlit.components.v1 as components


username = authenticate()
st.success("Logged in as {}".format(username))
PAGES = {
    "Dashboard": app1,
    "Reports": app2,
    "Timeline": app3,
    "Upload": app4
    # "Authentication": cyber_mads
}
st.title("Cyber MADS")
# components.html("<html><body><h1>Hello, World</h1></body></html>", width=200, height=200)
# st.sidebar.image(components.html("<html><body><h1>Hello, World</h1></body></html>", width=200, height=200), use_column_width=True)
st.sidebar.title('C-IDS')
# st.sidebar.button("Dashboard", list(PAGES.keys())
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()