import streamlit as st


def show_home():
    # st.title("Welcome to Resume-Reactor.")
    # intro = '''Essentially, Resume-Reactor is an AI-powered transformation engine for job seekers.
    #             It helps professionals convert long, detailed federal resumes into concise, ATS-friendly resumes for industry roles.
    #             Whether transitioning careers or optimizing your application, Resume-Reactor streamlines the process using AI.
    #             Upload your resume, paste a job description, and generate a polished resume—ready to download.
    #             Free to use.
    #             '''
    # st.markdown(intro)
    # st.image('assets/images/screenshot.png')
    
    # --- HEADER SECTION ---
    st.image("assets/images/RR_Logo_2dm.svg", use_container_width=True)
    st.image("assets/images/banner_image.webp", use_container_width=True)

    st.markdown(
        """
        <h2 style='text-align: center; font-size: 1.5em;'>Power Up Your Resume!</h2>
        <p style='text-align: center; font-size: 1.2em; color: gray;'>
            A streamlined AI-powered tool that transforms federal resumes into concise, ATS-optimized private-sector resumes—all in one click.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # # --- FEATURE HIGHLIGHTS ---
    # st.markdown(
    #     """
    #     ### ✨ Why Use ResumeReactor?
    #     ✅ **AI-powered resume optimization**  
    #     ✅ **Private-sector ready formatting**  
    #     ✅ **ATS-friendly and industry-aligned**  
    #     ✅ **One-click Word document download**  
    #     ✅ **No government jargon—just impactful, results-driven resumes**
    #     """,
    #     unsafe_allow_html=True,
    # )
