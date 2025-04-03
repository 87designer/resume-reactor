import streamlit as st
from modules.nav import Navbar

# Set up Streamlit page configuration
st.set_page_config(page_title="Resume Reactor - Create API Key", page_icon="🔑", layout="wide")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

Navbar()

HORIZONTAL_BLUE = "assets/images/RR_Logo.svg"
HORIZONTAL_WHITE = "assets/images/RR_Logo_dm.svg"

st.logo(HORIZONTAL_WHITE, icon_image=HORIZONTAL_WHITE)

# --- HEADER ---
st.markdown(
    """
    <h1 style='text-align: center;'>🔑 Creating an API Key</h1>
    <p style='text-align: center; font-size: 1.2em; color: gray;'>
        Step-by-step instructions to help you generate a API Key.
    </p>
    """,
    unsafe_allow_html=True,
)

# --- USER GUIDE SECTIONS ---
st.markdown(
    """
    ## 🧑‍🏫 How to Get Started with OpenAI for ResumeReactor

##### Create an API Key & Add Funds (Simple Step-by-Step)

ResumeReactor needs an OpenAI API key to work. Think of this key like a digital access pass to your personal AI assistant. It’s safe, private, and only used by you.
""")

with st.container(border=True):
    st.markdown(
        """
        ### ✅ Step 1: Create an OpenAI Account

    1.	Go to https://platform.openai.com/signup
    2.	Sign up using **your email, Google, or Microsoft account**
    3.	Once logged in, you’ll be taken to the **OpenAI Dashboard**


    ### 🔑 Step 2: Generate Your API Key
    
    1.	On the top-right corner, click your **profile icon**, then select **“API Keys”**
    Or go directly to: https://platform.openai.com/account/api-keys
    2.	Click the **“+ Create new secret key”** button
    3.	Give your key a name (like ResumeReactor) and click **Create key**
    4.	✅ **Copy the key** and save it somewhere (you won’t be able to see it again later)

    🔒 Keep your API key private – do not share it.

    ### 💵 Step 3: Add \$1–\$5 to Your Account

    OpenAI charges just a **few cents per resume**, so \$1–\$5 goes a long way.

    1.	Go to: https://platform.openai.com/account/billing/overview
    2.	Click **“Set up paid account”** or **“Add payment method”**
    3.	Add your credit card (OpenAI uses Stripe – it’s secure and widely trusted)
    4.	After payment method is added, click **“Usage Limits”**

    You can enter a **spending limit**, like \$5, to stay in control

    ### 🚀 Step 4: Paste Your API Key into ResumeReactor

    Once your API key is created and billing is set up:

    1.	Open ResumeReactor
    2.	Find the field that says **“Enter your OpenAI API Key”**
    3.	Paste in the key you copied
    4.	That’s it – you’re ready to generate resumes! 🎉
    """)

st.markdown(
    """
    ### 🤔 FAQs
    """)

with st.expander("Q: Is this safe?"):
    st.write('''
        Yes. Your key is used locally in your browser. Your resume data never leaves your machine unless you choose to send it.
    ''')

with st.expander("Q: How much does it cost?"):
    st.write('''
        Each resume usually costs less than 10 cents. \$1–\$5 is plenty to start with.
    ''')

with st.expander("Q: Can I cancel?"):
    st.write('''
        Yes! You can delete your API key or remove your payment method at any time.
    ''')
