import streamlit as st
from resume_analyzer import extract_text_from_pdf
import requests

# 🔐 DIRECTLY ADD YOUR API KEY HERE (not secure, just for testing)
GROQ_API_KEY = ""  # Replace with your actual Groq API key

# API and model setup
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-8b-8192"  # Or "llama3-70b-8192"

# Function to get feedback from Groq API
def get_resume_feedback_with_groq(resume_text):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Please analyze the following resume and provide only 5 short, complete bullet points of feedback.
Avoid repeating resume content. Make sure no bullet is cut off mid-sentence.
"You are a professional resume reviewer."
"Analyze the resume below and provide feedback in full bullet points."
"Make sure all sentences are *complete* and *not cut off*."
"You are a Resume Feedback Expert. Only answer resume-related questions. "
"Keep your answers short, complete, and clear "
"Do not include incomplete or trailing thoughts."
Resume:
{resume_text}
"""




    data = {
    "model": "llama3-8b-8192",
    "messages": [
        {
            "role": "system",
            "content": (
    "You are a professional resume reviewer. "
    "Return exactly 5 bullet points of feedback. "
    "Each bullet MUST start with • and be a complete, short sentence. "
    "Use newline breaks between each bullet point. "
    "Do NOT merge bullets into a paragraph. Do NOT omit bullet formatting."
   )
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.7,
    "max_tokens": 500,  # increase to allow full response
    # REMOVE this line 👇
    # "stop": ["\n", "User:", "Assistant:"]
}


    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error from Groq API: {response.status_code} - {response.text}"

# Streamlit UI
st.set_page_config(page_title="Resume AI Reviewer", page_icon="🤖")
st.title("🤖 Resume Feedback Bot")
st.markdown("Upload your *PDF resume* and get intelligent, tailored feedback using a Groq LLM.")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Analyzing with Groq AI..."):
        feedback = get_resume_feedback_with_groq(resume_text)

    st.subheader("AI Feedback")
    st.markdown(feedback)