import streamlit as st
from config import PAGE_CONFIG
from styles import apply_custom_styles
from components import render_sidebar,render_header, render_skills_input, render_job_cards, load_job_data_from_xml
from predict import load_unique_skills_from_xml

xml_file_path = 'data/unique_skills.xml'
unique_skills = load_unique_skills_from_xml(xml_file_path)
job_data = load_job_data_from_xml('data/job_data.xml')

def main():
    st.set_page_config(**PAGE_CONFIG)
    apply_custom_styles()
    
    render_header()
    render_sidebar()
    
    user_skills = render_skills_input(unique_skills)

    if 3 <= len(user_skills) <= 8:
        if st.button('Predict'):
            render_job_cards(job_data, user_skills)
    else:
        st.button('Predict', disabled=True)

if __name__ == "__main__":
    main()