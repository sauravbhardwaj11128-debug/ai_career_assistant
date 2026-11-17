# AI Career Agent

A Streamlit-based AI agent powered by Google's Gemini API.

## Features
- Resume Analyzer: strengths, gaps and improvement suggestions
- Job Role Finder: entry-level role recommendations and skill gaps
- Interview Coach: role-specific questions and sample answers
- Career Roadmap: weekly learning plan with measurable milestones

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```
5. Paste your Gemini API key in the sidebar.

Get a Gemini API key from https://aistudio.google.com/app/apikey

## Important
- Never upload your API key to GitHub.
- This is an AI-assisted guidance tool, not a recruiter or guaranteed job-placement service.
- Verify AI-generated advice before using it in applications.
\nThe app uses Google's Interactions API through the official Google Gen AI Python SDK.\n