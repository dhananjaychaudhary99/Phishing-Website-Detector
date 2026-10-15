import os
import sys
import joblib
import pandas as pd

sys.path.append(os.path.dirname(__file__))
from feature_extraction import extract_features

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "phishing_model.pkl")

def predict_url(url: str):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Run src/train.py first.")
    model = joblib.load(MODEL_PATH)
    features = extract_features(url)
    df_features = pd.DataFrame([features])
    prediction = int(model.predict(df_features)[0])
    probabilities = model.predict_proba(df_features)[0]
    return {
        "url": url,
        "is_phishing": bool(prediction == 1),
        "confidence": round(float(probabilities[prediction]), 4),
        "features": features
    }

if __name__ == '__main__':
    url_to_test = sys.argv[1] if len(sys.argv) > 1 else "http://secure-login-update-bank.com"
    print(predict_url(url_to_test))
