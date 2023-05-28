import random
import nltk
from nltk.chat.util import Chat, reflections

disease_data = {
    "diabetes": {
        "symptoms": "Frequent urination, increased thirst, unexplained weight loss, fatigue",
        "causes": "Insufficient production of insulin or inability to properly use insulin",
        "treatment": "Lifestyle changes, medication, insulin therapy"
    },
    "cancer": {
        "symptoms": "Unexplained weight loss, fatigue, lumps, changes in skin, persistent cough",
        "causes": "Genetic mutations, environmental factors, lifestyle choices",
        "treatment": "Surgery, chemotherapy, radiation therapy, immunotherapy"
    },
    "asthma": {
        "symptoms": "Shortness of breath, wheezing, chest tightness, coughing",
        "causes": "Environmental factors, allergies, genetics",
        "treatment": "Inhalers (bronchodilators, corticosteroids), avoiding triggers"
    },
    "alzheimer's disease": {
        "symptoms": "Memory loss, confusion, difficulty in problem-solving, mood swings",
        "causes": "Combination of genetic, lifestyle, and environmental factors",
        "treatment": "Medication, therapy, lifestyle modifications"
    },
    "heart disease": {
        "symptoms": "Chest pain, shortness of breath, fatigue, irregular heartbeat",
        "causes": "High blood pressure, smoking, high cholesterol, obesity",
        "treatment": "Lifestyle changes, medication, surgery"
    }
}

pairs = [
    (r'(?i)hi|hello|hola|wassup|namaste', ['Hello! How can I assist you today?']),
    (r'(?i)what are the symptoms of (.*)\??', [disease_data.get(disease.lower(), {}).get("symptoms", "I don't have information on that disease.") for disease in disease_data]),
    (r'(?i)what causes (.*)\??', [disease_data.get(disease.lower(), {}).get("causes", "I don't have information on that disease.") for disease in disease_data]),
    (r'(?i)what are the treatment options for (.*)\??', [disease_data.get(disease.lower(), {}).get("treatment", "I don't have information on that disease.") for disease in disease_data]),
    (r'(?i)bye|goodbye|exit|quit', ['Thank you for using the chatbot. Take care!']),
    (r'.*', ["I'm sorry, I don't have information on that disease."])
]

def chatbot():
    print("Welcome to the disease information chatbot! How can I assist you?")
    chat = Chat(pairs, reflections)
    chat.converse()

chatbot()
