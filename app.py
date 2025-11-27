import streamlit as st
from PIL import Image
import pytesseract

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

if st.button("Extract Skills"):
    if not job_desc:
        st.warning("Please provide a job description")
    else:
        # Placeholder skills (replace later with NLP extraction)
        skills = ["Python", "SQL", "Git"]
        categories = {
            "Programming": ["Python"],
            "Database": ["SQL"],
            "Tools": ["Git"]
        }
        roadmap = {
            "Python": ["Learn basics - 1 week", "Build projects - 2 weeks"],
            "SQL": ["Learn queries - 1 week", "Practice exercises - 3 days"],
            "Git": ["Learn basics - 1 day", "Version control practice - 2 days"]
        }

        st.subheader("Extracted Skills")
        st.write(skills)

        st.subheader("Categorized Skills")
        st.write(categories)

        st.subheader("Learning Roadmap")
        st.write(roadmap)
