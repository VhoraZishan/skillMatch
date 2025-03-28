import streamlit as st
from config import PRIMARY_COLOR, BACKGROUND_COLOR, SECONDARY_BG, TEXT_COLOR

def apply_custom_styles():
    custom_css = f"""
    <style>
        /* Base styles */
        .main {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}
        .stApp {{
            background-color: {BACKGROUND_COLOR};
        }}
        .sidebar .sidebar-content {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}
        .css-1d391kg {{
            padding-top: 3rem;
        }}
        
        /* Job Cards - Custom Style */
        .job-card {{
            background-color: #1A1A1A;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            border-left: 4px solid {PRIMARY_COLOR};
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }}
        .job-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 6px 12px {PRIMARY_COLOR}33; /* Primary color with 20% opacity */
        }}
        .job-title {{
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 12px;
            color: {PRIMARY_COLOR} !important;
        }}
        
        /* Skill tags */
        .skill-tag, .user-skill-tag {{
            background-color: #003333;
            color: {PRIMARY_COLOR} !important;
            padding: 5px 12px;
            border-radius: 15px;
            margin-right: 8px;
            margin-bottom: 8px;
            display: inline-block;
            font-size: 0.85rem;
            border: 1px solid {PRIMARY_COLOR};
        }}
        
        /* Match percentage */
        .match-percentage {{
            margin-top: 15px;
            font-size: 1.1rem;
            font-weight: bold;
            color: {PRIMARY_COLOR} !important;
        }}
        
        /* Rest of the existing styles */
        .app-header, .section-header {{
            color: {PRIMARY_COLOR};
        }}
        .app-header {{
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .section-header {{
            font-size: 24px;
            font-weight: bold;
            margin: 20px 0;
        }}
        .user-skills-section {{
            margin: 20px 0;
        }}
        label, .stTextInput label, .stMultiSelect label {{
            color: {PRIMARY_COLOR} !important;
            font-weight: bold !important;
            font-size: 16px !important;
        }}
        .stTextInput input, .stMultiSelect input {{
            color: {TEXT_COLOR} !important;
            background-color: #2D2D2D !important;
        }}
        .profile-section {{
            position: absolute;
            top: 20px;
            right: 20px;
            z-index: 1000;
        }}
        .stMultiSelect [data-baseweb="select"] {{
            background-color: #2D2D2D;
        }}
        .stMultiSelect [data-baseweb="select"] span {{
            color: {TEXT_COLOR};
        }}
        .stButton button {{
            background-color: {PRIMARY_COLOR} !important;
            color: black !important;
            font-weight: bold !important;
        }}
        
        [data-baseweb="menu"] {{
            background-color: #2D2D2D !important;
        }}
        [data-baseweb="menu"] li {{
            color: {TEXT_COLOR} !important;
        }}
        [data-baseweb="menu"] li:hover {{
            background-color: #3D3D3D !important;
        }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
