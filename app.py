import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "Reactor", "User Guide", "GitHub"]
selected = "Home"
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "assets/images/RR_Logo_dm.svg")
logo_page = None
urls = {"GitHub": "https://github.com/87designer/resume-reactor"}
styles = {
    "nav": {
        "background-color": "#0D152D",
        "justify-content": "left",
    },
    "img": {
        "padding": "20px",
    },
    "a": {
        "color": "#CD202A",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "hover": {
        "background-color": "#CD202A",
        "color": "#F8F9F6",
    },
    "active": {
        "background-color": "#F8F9F6",
        "color": "white",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
    "hide_nav": False,
    "fix_shadow": False,
}

page = st_navbar(
    pages,
    selected=selected,
    logo_path=logo_path,
    logo_page=logo_page,
    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Home": pg.show_home,
    "Reactor": pg.show_resume_reactor,
    "User Guide": pg.show_user_guide
}

go_to = functions.get(page)
if go_to:
    go_to()
