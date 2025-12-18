import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

st.set_page_config(page_title="SHL Assessment Tool", layout="wide")
st.title("SHL Assessment Recommender")

API_KEY = "AIzaSyC3EgmknWvv_wgcmHMFlbE2EFZqmqZSdAo"
genai.configure(api_key=API_KEY)

DATA_FILE = "Gen_AI Dataset.csv"

@st.cache_data
def get_knowledge_base():
    if not os.path.exists(DATA_FILE):
        return None
    
    try:
        df = pd.read_csv(DATA_FILE)
        return df.to_csv(index=False)
    except Exception as e:
        st.error(f"Error reading dataset: {e}")
        return None

knowledge_base = get_knowledge_base()

if not knowledge_base:
    st.error(f"Could not find or read '{DATA_FILE}'. Please ensure the file exists.")
    st.stop()

st.success("System Ready: Knowledge base loaded.")

job_description = st.text_area("Job Description / Requirements", height=150, 
                               placeholder="Paste the JD here (e.g., Senior Java Developer, 5 years exp, SQL required...)")

if st.button("Generate Recommendation"):
    if not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Analyzing requirements..."):
            try:
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                prompt = f"""
                Act as an expert SHL Assessment Consultant.
                
                Reference the TRAINING DATA below (historical queries and correct assessments) to recommend the best assessment for the NEW REQUEST.
                
                TRAINING DATA:
                {knowledge_base}
                
                NEW REQUEST:
                {job_description}
                
                OUTPUT INSTRUCTIONS:
                1. Identify the most suitable Assessment URL.
                2. Provide a brief justification linking specific skills in the JD to the assessment.
                """
                
                response = model.generate_content(prompt)
                
                st.subheader("Recommendation")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Generation failed: {e}")