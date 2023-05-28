import random

# Chatbot exit condition
global exit
exit = 0

def chatbot_response(user_questions):
    global exit
    DISEASES = {
        'COVID-19': {
            'overview': 'COVID-19 is a respiratory illness caused by the coronavirus.',
            'symptoms': 'Common symptoms include fever, cough, and difficulty breathing.',
            'treatment': 'There is currently no specific treatment for COVID-19. Supportive care and symptom management are provided.',
        },
        'INFLUENZA': {
            'overview': 'Influenza, also known as the flu, is a contagious respiratory illness caused by influenza viruses.',
            'symptoms': 'Symptoms include fever, cough, sore throat, muscle aches, and fatigue.',
            'treatment': 'Treatment involves rest, fluids, and over-the-counter pain relievers to relieve symptoms.',
        },
        'DIABETES': {
            'overview': 'Diabetes is a chronic condition that affects the way the body processes blood sugar.',
            'symptoms': 'Common symptoms include increased thirst, frequent urination, fatigue, and blurred vision.',
            'treatment': 'Treatment involves medication, insulin therapy, dietary changes, and regular physical activity.',
        },
        'HYPERTENSION': {
            'overview': 'Hypertension, or high blood pressure, is a condition in which the force of blood against artery walls is too high.',
            'symptoms': 'Hypertension is often asymptomatic, but it can lead to complications such as heart disease and stroke.',
            'treatment': 'Treatment includes lifestyle modifications (e.g., healthy diet, regular exercise) and medication.',
        },
        'ASTHMA': {
            'overview': 'Asthma is a chronic condition that affects the airways, causing inflammation and narrowing, which leads to difficulty breathing.',
            'symptoms': 'Common symptoms include wheezing, shortness of breath, chest tightness, and coughing.',
            'treatment': 'Treatment involves avoiding triggers, using inhalers (e.g., bronchodilators, corticosteroids), and managing underlying inflammation.',
        },
         'HEADACHE': {
            'overview': 'A headache is a common symptom characterized by pain or discomfort in the head or neck region.',
            'symptoms': 'Headaches can vary in intensity and may be accompanied by other symptoms such as sensitivity to light or sound.',
            'treatment': 'Treatment options for headaches include over-the-counter pain relievers, rest, and relaxation techniques.',
        },
    }

    user_questions = user_questions.upper()
    breakdown = list(user_questions.split(' '))
    print("Shinomiya:", end=" ")
    
    if any(disease in breakdown for disease in DISEASES):
        for disease in DISEASES:
            if disease in breakdown:
                print("Overview: " + DISEASES[disease]['overview'])
                print("Symptoms: " + DISEASES[disease]['symptoms'])
                print("Treatment: " + DISEASES[disease]['treatment'])
                break
        print("-----------------------------------------------")
    
    elif 'BYE' in breakdown or 'GOODBYE' in breakdown or 'CYA' in breakdown or 'EXIT' in breakdown:
        exit += 1
        print("Shinomiya: Happy to help! Have a great day!")
    
    elif 'HELLO' in breakdown or 'HI' in breakdown or 'HEY' in breakdown:
        greetings = ["Hello!", "Hi there!", "Hey! How can I assist you?"]
        print("Shinomiya:", random.choice(greetings))
        print("-----------------------------------------------")
    
    else:
        print("Shinomiya: I didn't understand your question.")
        print("-----------------------------------------------")
        

# Chatbot greetings
print("--------------Shinomiya---------------")
print("Hello and Greetings, I'm a Chatbot for Diseases.")
print("I can provide information about COVID-19, Influenza, Diabetes, Hypertension, and Asthma.")
print("How may I assist you?")

while exit != 1:
    user_input = input("You: ")
    if user_input.lower() != 'bye':
        chatbot_response(user_input)
    else:
        exit += 1
