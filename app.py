import streamlit as st
from PIL import Image
import pytesseract
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Job Skill Extractor & Learning Roadmap")

# Input type
input_type = st.radio("Upload Job Description as:", ["Text", "Image"])

job_desc = ""
if input_type == "Text":
    job_desc = st.text_area("Paste the Job Description here")
elif input_type == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        job_desc = pytesseract.image_to_string(image)

def extract_from_llm(text):
    prompt = f"""
    Extract the following from the job description:
    1. List of skills/tools/frameworks mentioned
    2. Categorize the skills into Programming, Tools, Databases, Soft Skills, etc.
    3. Create a beginner-friendly learning roadmap for each skill with duration.

    Return output in this JSON format:
    {{
      "skills": [...],
      "categories": {{...}},
      "roadmap": {{...}}
    }}

    Job Description:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content":prompt}],
        temperature=0
    )

    return response.choices[0].message.content

if st.button("Extract Skills"):
    if not job_desc:
        st.warning("Please provide a job description")
    else:
        output = extract_from_llm(job_desc)

        st.subheader("AI Output")
        st.write(output)

