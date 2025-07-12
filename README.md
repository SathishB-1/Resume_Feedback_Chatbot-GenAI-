## Project Title: Resume Feedback Bot using Groq LLM

## Description:

This project is a Streamlit web application that allows users to upload their resume in PDF format and receive intelligent, AI-generated feedback using Groq's LLaMA3 language model. The app extracts text from the uploaded PDF, sends it to the Groq API, and displays five short, complete bullet points of feedback.

## Features:

Upload PDF resumes

Extracts text from the resume

Sends data to Groq's LLaMA3-8B-8192 model via API

Returns exactly 5 professional bullet-point feedback items

Uses a clean and interactive Streamlit UI

## Technologies Used:

Python 3.8 or higher

Streamlit

Requests

Groq API (OpenAI-compatible)

PyMuPDF or similar PDF parser (used in resume_analyzer.py)

## Project Structure:

app.py Main Streamlit application

resume_analyzer.py Utility script for extracting text from PDF

requirements.txt Dependency list

README.txt This documentation file

## Installation and Setup:

Clone the repository:

git clone https://github.com/your-username/resume-feedback-bot.git

cd resume-feedback-bot

Install dependencies:

pip install -r requirements.txt

Add your Groq API key:

In app.py, replace the value of GROQ_API_KEY with your actual Groq key

## Run the application:
streamlit run app.py

## Sample Output:

• Resume highlights relevant experience, but lacks measurable achievements

• Improve formatting consistency in section headers and dates

• Add a professional summary to give recruiters context at a glance

• Tailor the skills section to match specific job descriptions

• Remove outdated or irrelevant information to keep the resume concise

## Notes:

Do not share your API key publicly

This tool is for educational and professional guidance only

You can deploy this project using Streamlit Cloud, Docker, or any hosting platform that supports Python apps

Author:

Developed by SATHISH B

GitHub:https://github.com/SathishB-1/Resume_Feedback_Chatbot