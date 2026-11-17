import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="AI Career Agent", page_icon="🤖", layout="wide")

st.title("🤖 AI Career Agent")
st.caption("An AI-powered career assistant for resume insights, job matching, interview preparation and career planning.")

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Gemini API key", type="password", help="Get a key from Google AI Studio.")
    model_name = st.selectbox("Gemini model", ["gemini-3.8-flash"], index=0)
    st.info("Your API key is used only for requests from this app. Do not share it or commit it to GitHub.")

def ask_agent(task, details):
    if not api_key:
        st.error("Please enter your Gemini API key in the sidebar.")
        return None
    try:
        client = genai.Client(api_key=api_key)
        prompt = f"""
You are CareerPilot, a practical and honest AI career agent.
Task: {task}
User information:
{details}

Instructions:
- Give specific, realistic and actionable advice.
- Do not invent qualifications, experience, job openings, salaries or certifications.
- If information is missing, clearly state assumptions and ask for what is needed.
- Use clear headings, concise bullet points and a helpful professional tone.
"""
        interaction = client.interactions.create(
            model=model_name,
            input=prompt,
        )
        return interaction.output_text
    except Exception as e:
        st.error(f"Gemini request failed: {e}")
        st.caption("Check your API key, internet connection, model availability and API quota.")
        return None

tab1, tab2, tab3, tab4 = st.tabs([
    "📄 Resume Analyzer", "🎯 Job Role Finder", "🎤 Interview Coach", "🗺️ Career Roadmap"
])

with tab1:
    st.subheader("Resume Analyzer")
    resume = st.text_area("Paste your resume text", height=220, placeholder="Paste resume content here...")
    if st.button("Analyze Resume", key="resume"):
        if resume.strip():
            with st.spinner("Analyzing your resume..."):
                result = ask_agent("Analyze this resume. Identify strengths, missing skills, improvement points and an improved professional summary.", resume)
            if result: st.markdown(result)
        else: st.warning("Please paste your resume text first.")

with tab2:
    st.subheader("Job Role Finder")
    skills = st.text_area("Your skills", placeholder="Example: Python, SQL, Machine Learning, Streamlit")
    education = st.text_input("Education", placeholder="Example: B.Tech in AI & Data Science")
    interests = st.text_input("Interests", placeholder="Example: Generative AI, data science")
    if st.button("Find Suitable Roles", key="roles"):
        details = f"Skills: {skills}\nEducation: {education}\nInterests: {interests}"
        if skills.strip() or interests.strip():
            with st.spinner("Finding suitable roles..."):
                result = ask_agent("Suggest suitable entry-level job roles, explain why they fit, list skill gaps and suggest portfolio projects.", details)
            if result: st.markdown(result)
        else: st.warning("Enter at least your skills or interests.")

with tab3:
    st.subheader("Interview Coach")
    role = st.text_input("Target job role", placeholder="Example: AI/ML Intern")
    level = st.selectbox("Experience level", ["Fresher", "Internship", "0-2 years", "Experienced"])
    if st.button("Generate Interview Practice", key="interview"):
        if role.strip():
            with st.spinner("Preparing your interview session..."):
                result = ask_agent("Create 10 role-specific interview questions with concise sample answers, followed by 5 HR questions and tips. Keep the level appropriate.", f"Target role: {role}\nLevel: {level}")
            if result: st.markdown(result)
        else: st.warning("Enter a target job role.")

with tab4:
    st.subheader("Personalized Career Roadmap")
    goal = st.text_input("Your career goal", placeholder="Example: Become a Generative AI Developer")
    hours = st.slider("Hours available per week", 1, 40, 10)
    duration = st.selectbox("Planning period", ["2 weeks", "1 month", "3 months", "6 months"])
    if st.button("Create My Roadmap", key="roadmap"):
        if goal.strip():
            with st.spinner("Building your roadmap..."):
                result = ask_agent("Create a practical learning roadmap with weekly milestones, hands-on tasks, measurable outcomes and a final portfolio deliverable.", f"Goal: {goal}\nAvailable time: {hours} hours/week\nDuration: {duration}")
            if result: st.markdown(result)
        else: st.warning("Enter your career goal.")

st.divider()
st.caption("AI Career Agent | Built with Python, Streamlit and Google Gemini API")
