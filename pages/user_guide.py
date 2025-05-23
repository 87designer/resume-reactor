import streamlit as st
from modules.nav import Navbar

# Set up Streamlit page configuration
st.set_page_config(page_title="Resume Reactor - User Guide", page_icon="📖", layout="wide")

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
    <h1 style='text-align: center;'>📖 ResumeReactor User Guide</h1>
    <p style='text-align: center; font-size: 1.2em; color: gray;'>
        Step-by-step instructions to help you generate a private-sector resume effortlessly.
    </p>
    """,
    unsafe_allow_html=True,
)

# --- USER GUIDE SECTIONS ---
st.markdown(
    """
    ## 📌 Getting Started  
    Welcome to **ResumeReactor**! Follow this step-by-step guide to transform your **federal resume** into an **ATS-friendly private-sector resume**.
    """,
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown("### 🛠️ Step 1: Enter Your Information")
    st.write("- Fill in your **name** and **contact details**.")
    st.write("- Paste your **OpenAI API key** (required for AI-powered resume generation).")

    st.markdown("### 📂 Step 2: Upload Your Resume")
    st.write("- Supported formats: **TXT, DOCX**.")
    st.write("- Ensure your federal resume is **formatted properly** with clear sections.")

    st.markdown("### 📝 Step 3: Paste the Job Description")
    st.write("- Copy & paste the **job posting** you’re applying for.")
    st.write("- The AI will **analyze and optimize your resume** to match the job description.")

    st.markdown("### 🚀 Step 4: Generate Your Resume")
    st.write("- Click **'Generate Resume'** to create a **concise, industry-aligned** version.")
    st.write("- A **preview** of the new resume will appear below.")

    st.markdown("### 💾 Step 5: Download Your Resume")
    st.write("- Click **'Download Word Document'** to save your **.docx file**.")
    st.write("- Your resume is now ready for the Final Touches! 🎉")

# --- TROUBLESHOOTING & FINAL TIPS ---
st.markdown("## ⚠️ Final Touches & Troubleshooting")

with st.expander("✅ Proofread Before You Submit"):
    st.write("- The resume generated by ResumeReactor is designed to get you **90% of the way there**.")
    st.write("- Always **proofread** the final output for tone, clarity, and grammar.")
    st.write("- Carefully **spot-check for any responsibilities or achievements** the AI may have inferred from the job description that you **haven’t actually done**.")
    st.write("- You are responsible for ensuring everything on your resume is **truthful and accurate**.")

with st.expander("🎨 Formatting Adjustments"):
    st.write("- You can make small edits to the downloaded **Word document**.")
    st.write("- Adjust spacing, bolding, or alignment as needed to match your personal style.")

with st.expander("🚧 Common Issues"):
    st.write("- Ensure your **OpenAI API key** is valid and has enough quota.")
    st.write("- Upload only **.txt** or **.docx** resumes — not PDFs or scanned files.")
    st.write("- If content seems off, try simplifying the job description or trimming your resume before upload.")
