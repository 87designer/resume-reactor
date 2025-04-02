import os
import streamlit as st
from modules.nav import Navbar

st.set_page_config(page_title="Resmue-Reactor - Home",
                   page_icon="📈",
                   layout="wide",
                   )

Navbar()

HORIZONTAL_BLUE = "assets/images/RR_Logo.svg"
HORIZONTAL_WHITE = "assets/images/RR_Logo_dm.svg"

st.logo(HORIZONTAL_BLUE, icon_image=HORIZONTAL_WHITE)



# -----------------------------------------------------------
# SIDEBAR
# st.sidebar.markdown("Hi!")

# -----------------------------------------------------------
# CONTENT
col1, col2, col3 = st.columns([1, 2, 1])

col2.image("assets/images/banner_image.webp", use_container_width=True)

col2.markdown(
    """
    <h2 style='text-align: center; font-size: 1.5em;'>Power Up Your Resume!</h2>
    <p style='text-align: center; font-size: 1.2em; color: gray;'>
        A streamlined AI-powered tool that transforms federal resumes into concise, ATS-optimized private-sector resumes—all in one click.
    </p>
    """,
    unsafe_allow_html=True,
)

# col2.image("assets/images/RR_Logo_2dm.svg", width=200)