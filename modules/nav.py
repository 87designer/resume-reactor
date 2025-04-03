import streamlit as st


def Navbar():
    with st.sidebar:
        st.sidebar.subheader("Navigation")
        st.page_link('app.py', label='Home', icon='🚀')
        st.page_link('pages/reactor.py', label='Tailor Resume', icon='🪡')
        st.page_link('pages/user_guide.py', label='User Guide', icon='📖')
        st.page_link('pages/how_to.py', label='Create API Key', icon='🔑')
        
        st.sidebar.subheader("External Links")
        st.page_link('https://github.com/87designer/resume-reactor', label='GitHub', icon='👨‍💻')
        # st.sidebar.markdown("🔒 Locked Page")