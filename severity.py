import joblib

severity_model = joblib.load("Models/severity_model_firms.pkl")

def compute_severity(features):
    return severity_model.predict([features])[0]