import pandas as pd
import joblib
import os
import xml.etree.ElementTree as ET

MODEL_PATH = os.path.join('models', 'rfmodel.pkl')
TFIDF_PATH = os.path.join('models', 'tfidf.pkl')
DATASET_PATH = os.path.join('data', 'job_dataset.csv')

def load_unique_skills_from_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    unique_skills = []
    for skill in root.findall('Skill'):
        unique_skills.append(skill.text.strip())

    return unique_skills

def load_model_and_vectorizer():
    rf_model = joblib.load(MODEL_PATH)
    tfidf = joblib.load(TFIDF_PATH)
    return rf_model, tfidf

def load_y_train():
    data = pd.read_csv(DATASET_PATH)
    
    y_train = data['Title']
    
    y_train = y_train.astype('category')
    
    return y_train

unique_skills_list = load_unique_skills_from_xml('data/unique_skills.xml')

def predict_top_3_titles(skills, rf_model, tfidf, y_train):
    filtered_data = [skill for skill in skills if skill and skill in unique_skills_list]

    if not filtered_data:
        return "No valid skills were provided."

    combined_skills = ' '.join(filtered_data)

    input_tfidf = tfidf.transform([combined_skills])

    predicted_probs = rf_model.predict_proba(input_tfidf)

    top_3_indices = predicted_probs[0].argsort()[-3:][::-1]
    top_3_titles = y_train.astype('category').cat.categories[top_3_indices]
    top_3_probs = predicted_probs[0][top_3_indices] * 100

    top_3_results = [(title, f"{prob:.2f}%") for title, prob in zip(top_3_titles, top_3_probs)]
    
    return top_3_results