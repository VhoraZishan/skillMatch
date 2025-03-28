import streamlit as st
from config import PRIMARY_COLOR, TEXT_COLOR, SECONDARY_BG
import xml.etree.ElementTree as ET
from predict import load_model_and_vectorizer, predict_top_3_titles, load_y_train

def load_job_data_from_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    job_data = []
    for job in root.findall('Job'):
        job_title = job.get('title')
        skills = [skill.text.strip() for skill in job.find('Skills').findall('Skill')]
        job_data.append({
            "title": job_title,
            "skills": skills
        })

    return job_data

def render_header():
    st.markdown(
        '<div style="margin-top: 50px; text-align: center;">'
        f'<h2 style="color: {PRIMARY_COLOR};">Enter your skills below</h2>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)

def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="app-header">skillMatch</div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f'<div style="color: {PRIMARY_COLOR}; font-weight: bold;">Dashboard</div>', unsafe_allow_html=True)
        
        
        
        st.markdown("---")
        st.markdown(f"""
        <div style="text-align: center; color: {PRIMARY_COLOR} !important;">
            <h1>Developed By</h1><br>
            <strong>Kunal Chauhan</strong><br>
            <strong>Yash Dave</strong><br>
            <strong>Zishan Vhora</strong>
        </div>
        """, unsafe_allow_html=True)

def render_skills_input(unique_skills):
    user_skills = st.multiselect("Enter your skills (Choose between 3 and 8 skills)", unique_skills)

    if len(user_skills) < 3:
        st.warning("Please select at least 3 skills.")
    elif len(user_skills) > 8:
        st.warning("You can select a maximum of 8 skills.")

    st.markdown('</div>', unsafe_allow_html=True)

    if 3 <= len(user_skills) <= 8:
        st.markdown('<div class="user-skills-section">', unsafe_allow_html=True)
        skills_html = "".join([f'<span class="user-skill-tag">{skill}</span> ' for skill in user_skills])
        st.markdown(skills_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    return user_skills

def render_job_cards(job_data, user_skills):
    rf_model, tfidf = load_model_and_vectorizer()

    y_train = load_y_train()
    top_3_results = predict_top_3_titles(user_skills, rf_model, tfidf, y_train)

    if isinstance(top_3_results, str):
        st.info(top_3_results)
        return

    filtered_jobs = []
    for title, prob in top_3_results:
        for job in job_data:
            if job["title"] == title:
                job_copy = job.copy()
                job_copy["match_percentage"] = prob
                filtered_jobs.append(job_copy)

    st.markdown('<div class="section-header">Recommended Jobs</div>', unsafe_allow_html=True)
    
    cols = st.columns(3)

    for i, job in enumerate(filtered_jobs):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="job-card">
                <div class="job-title">{job["title"]}</div>
                <div class="skills-list">
                    {"".join([f'<span class="skill-tag">{skill}</span>' for skill in job["skills"]])}
                </div>
                <div class="match-percentage">{job["match_percentage"]} Match</div>
            </div>
            """, unsafe_allow_html=True)

    if user_skills and not filtered_jobs:
        st.info("No jobs match your predicted titles. Try adding more skills or different ones.")
