# SHL Assessment Recommendation Engine

## Project Overview
The **SHL Assessment Recommendation Engine** is a specialized Generative AI web application designed to streamline the recruitment process for HR professionals and talent acquisition teams. In the complex landscape of talent assessment, selecting the precise test for a specific job description—ranging from technical skills like Java and SQL to soft skills like leadership and communication—can be time-consuming and prone to error.

This project addresses that challenge by automating the selection process using advanced Large Language Model (LLM) capabilities. By leveraging **Google’s Gemini 2.5 Flash** model and a tailored **Retrieval-Augmented Generation (RAG)** approach, the tool matches job descriptions against a historical dataset of verified assessments to provide accurate, data-driven recommendations.

## Key Features
- **AI-Powered Recommendations:** Uses the Gemini 2.5 Flash model to analyze Job Descriptions (JDs) and find the best matching SHL assessment.
- **Context-Aware Logic:** Provides a "Justification" for every recommendation, explaining exactly which skills in the JD led to the specific test selection.
- **Historical Knowledge Base:** Powered by a CSV dataset (`Gen_AI Dataset.csv`) containing real-world examples of past queries and correct answers.
- **Simple Web Interface:** Built with **Streamlit**, offering a clean and responsive UI for recruiters to easily input requirements.

## Technology Stack
- **Language:** Python 3.10+
- **Frontend:** Streamlit
- **AI Model:** Google Gemini 2.5 Flash (via `google-generativeai`)
- **Data Handling:** Pandas

## How to Setup the Project
Follow these steps to set up the project on your local machine.

### Prerequisite
You must have **Python** installed. You can check by running `python --version` in your terminal.

### Step 1: Download the Files
1. Create a new folder named `shl-recommender`.
2. Place `app.py`, `Gen_AI Dataset.csv`, and `requirements.txt` inside this folder.

### Step 2: Create a Virtual Environment (Recommended)
It is best practice to run Python projects in a virtual environment to avoid conflicts.
* **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
* **Mac/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### Step 3: Install Dependencies
With your virtual environment active, install the required libraries:
```bash
pip install -r requirements.txt
```

### Screenshot
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/b7332ee7-7ca5-43e1-8e84-f8345d3047ab" />
