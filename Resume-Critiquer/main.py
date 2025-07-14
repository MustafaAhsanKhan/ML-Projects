import streamlit as st
import PyPDF2
import os
import io
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon=":guardsman:", layout="centered")

st.title("AI Resume Critiquer")

st.markdown("Upload your resume in PDF format, and the AI will provide feedback on how to improve it.")

api_keu = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Choose a PDF/TXT file", type=["pdf", "txt"])

job_role = st.text_input("Enter the job role you are applying for")

analyze_button = st.button("Analyze Resume")

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_file(file):
    if file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(file.read()))
    elif file.type == "text/plain":
        return file.read().decode("utf-8")  # Decoding text file




if analyze_button and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)
        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read. Please upload a valid PDF or TXT file.")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}
    
        Resume content:
        {file_content}
    
        Please provide your analysis in a clear, structured format with specific recommendations."""
    
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            )
        
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528:free",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer."},
                {"role": "user", "content": prompt}
            ],
            #stream = True,
            temperature=0.7,
            max_tokens=1500
        )
        st.markdown("### AI Feedback:")
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")


