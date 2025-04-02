import streamlit as st


def Navbar():
    with st.sidebar:
        st.sidebar.subheader("Navigation")
        st.page_link('app.py', label='Home', icon='💻')
        st.page_link('pages/reactor.py', label='Tailor Resume', icon='📄')
        # st.page_link('pages/user_guide.py', label='Skills', icon='🛠️')
        
        st.sidebar.subheader("Coming Soon")
        st.sidebar.markdown("🔒 User Guide")
        st.sidebar.markdown("🔒 Create an API Key")