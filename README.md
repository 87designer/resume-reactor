# ResumeReactor

## 🚀 Overview
ResumeReactor is a **Streamlit-powered application** that transforms **federal resumes** into **concise, ATS-optimized private-sector resumes**. It uses **OpenAI's GPT-4** to analyze job descriptions and craft tailored resumes that align with industry-specific expectations.

## 🎯 Features
- **AI-Powered Resume Generation**: Converts federal resumes into private-sector resumes with **optimized formatting**.
- **Markdown-Based Resume Structuring**: Ensures that headers, bullet points, and key formatting elements are properly handled.
- **ATS-Friendly Output**: Prioritizes **concise bullet points, quantifiable achievements, and professional formatting**.
- **Industry-Specific Optimization**: Adapts resumes based on **user-defined industries** (e.g., IT, Finance, Healthcare, Government Contracting).
- **Custom Contact Information Handling**: Dynamically **includes only provided contact details** in the resume header.
- **One-Click Word Document Export**: Allows users to **download the formatted resume** as a .docx file.

## 🛠️ Installation
### Prerequisites
Ensure you have **Python 3.8+** installed.

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/87designer/resume-reactor.git
cd resume-reactor
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```sh
streamlit run app.py
```

## 📌 Usage
### 1️⃣ Provide Input Data
- Enter your **OpenAI API key**.
- Fill in your **name and contact information**.
- Upload your **federal resume (TXT or DOCX format)**.
- Paste the **job description**.
- Specify the **target industry**.

### 2️⃣ Generate Resume
- Click **"Generate Resume"** to process the information.
- View the **AI-generated resume preview**.
- Click **"Download Word Document"** to save the resume as a `.docx` file.

## 🏗️ Project Structure
```
resume-reactor/
│-- app.py                  # Streamlit app for UI and AI-powered resume generation
│-- requirements.txt        # Required dependencies
│-- README.md               # Project documentation
```

## 🔑 API Key Setup
ResumeReactor uses **OpenAI's API** for resume transformation. Obtain an API key by following these steps:
1. Visit [OpenAI](https://platform.openai.com/signup/).
2. Sign in or create an account.
3. Navigate to **API Keys**.
4. Generate a new key and copy it.
5. Paste it into the **OpenAI API Key** field in ResumeReactor.

## 🛡️ License
This project is licensed under the **GNU General Public License v3.0 (GPLv3)**. 

You are free to use, modify, and distribute this software under the terms of the GPLv3 license. 
For more details, see the full license text at [GNU Licenses](https://www.gnu.org/licenses/gpl-3.0.html).

## 🤝 Contributing
Contributions are welcome! To contribute:
1. **Fork** the repository.
2. Create a **feature branch** (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -m 'Add feature XYZ'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a **Pull Request**.

## 📧 Contact
For inquiries, reach out via **cgdesigned@gmail.com** or create an **Issue** in the repository.

---

🚀 **ResumeReactor** – Helping federal employees transition into the private sector seamlessly!

