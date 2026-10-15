import os
import sys
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

sys.path.append(os.path.dirname(__file__))
from feature_extraction import extract_dataframe

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "dataset.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "phishing_model.pkl")

def train():
    df = pd.read_csv(RAW_DATA_PATH)
    X = extract_dataframe(df['url'].tolist())
    y = df['label']

    processed_df = X.copy()
    processed_df['label'] = y
    processed_df.to_csv(PROCESSED_DATA_PATH, index=False)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, preds):.2f}')
    print(classification_report(y_test, preds, zero_division=0))

    joblib.dump(model, MODEL_PATH)
    print(f'Model saved at {MODEL_PATH}')

if __name__ == '__main__':
    train()
