def diagnose(symptoms_input):
    disease_info = {
        "Common Cold": {
            "symptoms": ["cough", "sneezing", "runny nose", "sore throat", "mild fever"],
            "treatments": ["Rest", "Stay hydrated", "Use over-the-counter medications for symptoms", "Warm saltwater gargle for sore throat"]
        },
        "Flu": {
            "symptoms": ["fever", "chills", "body ache", "cough", "fatigue"],
            "treatments": ["Rest", "Flu medication (antiviral)", "Hydration", "Pain relievers"]
        },
        "COVID-19": {
            "symptoms": ["fever", "dry cough", "fatigue", "loss of taste", "shortness of breath"],
            "treatments": ["Rest", "Hydration", "Paracetamol for fever", "Consult a doctor for severe symptoms"]
        },
        "Malaria": {
            "symptoms": ["fever", "chills", "sweating", "headache", "nausea"],
            "treatments": ["Antimalarial drugs", "Rest", "Hydration"]
        },
        "Dengue": {
            "symptoms": ["high fever", "severe headache", "pain behind eyes", "joint pain", "rash"],
            "treatments": ["Rest", "Hydration", "Pain relievers (avoid aspirin)", "Consult a doctor for severe cases"]
        },
        "Typhoid": {
            "symptoms": ["fever", "abdominal pain", "diarrhea", "weakness", "loss of appetite"],
            "treatments": ["Antibiotics", "Rest", "Hydration", "Avoid spicy foods"]
        },
        "Migraine": {
            "symptoms": ["severe headache", "nausea", "sensitivity to light", "blurred vision"],
            "treatments": ["Pain relievers", "Rest in a dark room", "Stay hydrated", "Consult a doctor for prescribed migraine medication"]
        }
    }

    MIN_INPUT = 2
    MAX_INPUT = 6

    if len(symptoms_input) < MIN_INPUT:
        return "Please provide at least 2 symptoms for accurate diagnosis."
    if len(symptoms_input) > MAX_INPUT:
        return f"Too many symptoms. Please limit to {MAX_INPUT} for best results."

    matched_diseases = []

    for disease, info in disease_info.items():
        match_count = len(set(symptoms_input).intersection(set(info["symptoms"])))
        confidence = match_count / len(info["symptoms"])
        if match_count >= MIN_INPUT:
            matched_diseases.append((disease, confidence, info["symptoms"], info["treatments"]))

    if not matched_diseases:
        return "No disease could be confidently diagnosed with the given symptoms."

    result = "Possible Diagnoses (with confidence levels, symptoms, and treatments):\n"
    for disease, confidence, symptoms, treatments in matched_diseases:
        result += f"\n  - {disease}: {round(confidence * 100)}% match\n"
        result += f"    Symptoms: {', '.join(symptoms)}\n"
        result += f"    Treatments: {', '.join(treatments)}\n"

    # Add message after diagnosing
    result += "\nPlease remember, this is a general diagnosis based on symptoms provided.\n"
    result += "For a precise diagnosis and treatment plan, consult with a healthcare professional."

    return result

def main():
    print("\n  Welcome to the Medical Diagnosis Expert System")
    print("Enter your symptoms separated by commas (e.g., fever, cough):")

    user_input = input("Symptoms: ").lower()
    symptoms_list = [sym.strip() for sym in user_input.split(",") if sym.strip()]

    print("\n Diagnosing...")
    result = diagnose(symptoms_list)
    print(result)

if __name__ == "__main__":
    main()
