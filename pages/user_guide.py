import streamlit as st


def show_user_guide():
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
    st.write("- Your resume is now ready for submission! 🎉")

    # --- TROUBLESHOOTING SECTION ---
    st.markdown("## ⚠️ Troubleshooting Common Issues")

    st.markdown("#### ❌ API Key Issues")
    st.write("- Ensure your **OpenAI API key** is **valid and active**.")
    st.write("- Check your **OpenAI account** for **quota limits**.")
    st.write("- If you get a **rate limit error (429)**, wait a few minutes before retrying.")

    st.markdown("#### 📂 File Upload Issues")
    st.write("- Only **TXT and DOCX** files are supported.")
    st.write("- Ensure your resume is **not password-protected**.")

    st.markdown("#### 📝 Formatting Issues")
    st.write("- Resume text may be too long—try **removing unnecessary details**.")
    st.write("- Ensure **headers, bullet points, and sections are clear** for best results.")

    # --- SUPPORT CTA ---
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <a href='#' style='
                display: inline-block;
                background-color: #FF5733;
                color: white;
                padding: 12px 24px;
                font-size: 1.2em;
                font-weight: bold;
                text-decoration: none;
                border-radius: 8px;
            '>
            🔹 Contact Support
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
