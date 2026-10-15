Set-Content -Path "README.md" -Encoding utf8 -Value @'
# 🛡️ Phishing Website Detector — ML-Based URL Classification

A machine learning-based cybersecurity application that analyzes URLs and classifies them as potentially legitimate or phishing using lexical, structural, and statistical URL features. Built with **Python, Flask, and a Random Forest classifier**, the project is designed to support URL analysis through a web dashboard, command-line predictions, heuristic security diagnostics, and a REST API where implemented.

The application is intended for defensive cybersecurity analysis. Predictions are advisory and do not guarantee that a website is safe or malicious.

---

## 🌐 Live Demo

🔗 **Live Website:** [Phishing Website Detector](https://dhananjaychaudhary99.github.io/Phishing-Website-Detector/)

📂 **Source Code:** [GitHub Repository](https://github.com/dhananjaychaudhary99/Phishing-Website-Detector)

🚀 **Hosting:** GitHub Pages  
🔒 **HTTPS:** Enabled

> **Deployment note:** GitHub Pages hosts static files and does not execute Python or Flask. If the application requires a Flask backend for model predictions, deploy that backend separately and configure the frontend to call its HTTPS API.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [System Architecture](#system-architecture)
- [How It Works](#how-it-works)
- [Installation and Setup](#installation-and-setup)
- [Training the Model](#training-the-model)
- [Making Predictions](#making-predictions)
- [Launching the Web Application](#launching-the-web-application)
- [REST API](#rest-api)
- [Feature Engineering](#feature-engineering)
- [Testing](#testing)
- [Security Considerations](#security-considerations)
- [Limitations](#limitations)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 📌 Overview

Phishing attacks use deceptive URLs and websites to trick users into revealing passwords, financial information, and other sensitive data. This project explores how machine learning and URL-based feature engineering can help identify suspicious links.

The application processes URL characteristics, converts them into features, and uses a trained classification model to predict a URL's category. Depending on the implementation, results may also include heuristic warnings and diagnostic information.

### 🎯 Project Objectives

- Identify potentially suspicious URLs through automated classification.
- Apply machine learning to lexical and structural URL characteristics.
- Present classification results through a user-friendly interface.
- Support command-line and API-based predictions where implemented.
- Separate feature extraction, training, inference, and presentation logic.
- Promote awareness of phishing attacks and safer browsing practices.

---

## ✨ Key Features

- **URL Feature Extraction:** Extracts configured characteristics such as URL length, hostname structure, and suspicious patterns.
- **Machine Learning Classification:** Uses a trained Random Forest model, if provided by the implementation.
- **Security Diagnostics:** Supports heuristic warnings for configured suspicious URL patterns.
- **Web Dashboard:** Provides a browser-based interface when the frontend is connected to the application.
- **Command-Line Predictions:** Supports terminal-based analysis if a CLI is implemented.
- **REST API:** Enables JSON-based integration if the corresponding endpoints are implemented.
- **Model Persistence:** Allows a trained model to be saved and reused for inference.
- **Data Processing:** Supports dataset preparation and feature extraction.
- **Automated Testing:** Supports regression testing using pytest when tests are available.
- **Modular Architecture:** Organizes application responsibilities into reusable components.

> Feature availability depends on the files and configuration present in the repository.

---

## 🧰 Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python 3.10+ |
| Web Framework | Flask |
| Machine Learning | scikit-learn |
| Classification Algorithm | Random Forest |
| Data Processing | pandas, NumPy |
| Domain Parsing | tldextract, if used |
| Model Persistence | joblib or the configured serialization method |
| Domain Registration Lookup | python-whois, if implemented |
| Database | SQLite, if scan logging is implemented |
| Testing | pytest |
| Version Control | Git and GitHub |
| Static Hosting | GitHub Pages |
| CI/CD | GitHub Actions, if configured |

Use the versions and dependencies defined in the actual project configuration.

---

## 📁 Project Structure

The following is a reference layout for the project. Existing filenames and directories may differ.

\`\`\`text
Phishing-Website-Detector/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── dataset.csv
│   └── processed/
│       └── cleaned_data.csv
│
├── models/
│   └── phishing_model.pkl
│
├── src/
│   ├── __init__.py
│   ├── feature_extraction.py
│   ├── train.py
│   └── predict.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   └── index.html
│
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py
│
├── scans.db
│
└── .github/
    └── workflows/
        └── test.yml
\`\`\`

### Important Files

| File | Responsibility |
|---|---|
| `app.py` | Flask routes, web interface, and API endpoints |
| `requirements.txt` | Python dependency definitions |
| `src/feature_extraction.py` | Extracts URL features |
| `src/train.py` | Trains the classification model |
| `src/predict.py` | Provides prediction functionality |
| `models/phishing_model.pkl` | Example serialized model artifact |
| `data/raw/dataset.csv` | Example source dataset |
| `templates/index.html` | HTML dashboard template |
| `static/css/style.css` | Dashboard styling |
| `static/js/main.js` | Frontend interactions |
| `tests/test_pipeline.py` | Example automated tests |
| `scans.db` | Optional SQLite scan history |
| `.github/workflows/test.yml` | Optional CI workflow |

**Note:** Do not assume these files exist. Check the repository before running commands that depend on them.

---

## 🏗️ System Architecture

\`\`\`text
              ┌──────────────────────┐
              │      User Input      │
              │    Web / CLI / API   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Input Validation   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Feature Extraction  │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Trained ML Classifier│
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Classification     │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Results and Warnings │
              └──────────────────────┘
\`\`\`

### Processing Pipeline

1. Receive a URL through the dashboard, CLI, or API.
2. Validate and normalize the input.
3. Extract the features expected by the trained model.
4. Generate a classification using the saved model.
5. Evaluate configured heuristic checks, if available.
6. Return the prediction and applicable diagnostics.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a version supported by the project dependencies.
- Git.
- pip.

Verify the installations in PowerShell:

\`\`\`powershell
python --version
python -m pip --version
git --version
\`\`\`

### 1. Clone the Repository

\`\`\`powershell
git clone https://github.com/dhananjaychaudhary99/Phishing-Website-Detector.git
Set-Location Phishing-Website-Detector
\`\`\`

### 2. Create a Virtual Environment

\`\`\`powershell
python -m venv .venv
\`\`\`

### 3. Activate the Environment

\`\`\`powershell
.\.venv\Scripts\Activate.ps1
\`\`\`

If PowerShell blocks activation, allow scripts for the current terminal session:

\`\`\`powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
\`\`\`

### 4. Install Dependencies

If `requirements.txt` exists:

\`\`\`powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
\`\`\`

### 5. Inspect the Project Files

\`\`\`powershell
Get-ChildItem
Get-ChildItem src
Get-ChildItem models
\`\`\`

Confirm the actual dataset, model artifact, training script, and application entry point before proceeding.

---

## 🤖 Training the Model

If the repository contains `src/train.py`, run:

\`\`\`powershell
python src\train.py
\`\`\`

A typical training workflow includes:

1. Load the labeled URL dataset.
2. Validate and prepare the data.
3. Extract features using the project's feature extraction implementation.
4. Split the dataset into training and testing sets.
5. Train the Random Forest classifier.
6. Evaluate the model on held-out data.
7. Save the trained model to the configured output path.

Example paths, depending on the implementation:

\`\`\`text
data/raw/dataset.csv
data/processed/cleaned_data.csv
models/phishing_model.pkl
\`\`\`

### Model Evaluation

| Metric | Purpose |
|---|---|
| Accuracy | Proportion of all predictions that are correct |
| Precision | Proportion of predicted phishing URLs that are actually phishing |
| Recall | Proportion of phishing URLs correctly identified |
| F1-score | Harmonic mean of precision and recall |
| Confusion Matrix | Shows correct classifications, false positives, and false negatives |

For phishing detection, evaluate false negatives and false positives carefully. Accuracy alone does not establish that a model is reliable.

No performance score is claimed in this README.

---

## 🔎 Making Predictions

### Command-Line Interface

If `src/predict.py` accepts a URL as a positional argument, use:

\`\`\`powershell
python src\predict.py "https://example.com/login"
\`\`\`

Replace the example URL with the URL you want to analyze.

If the script requires different arguments, follow its implemented command-line interface.

### Python Integration

A reusable prediction function can be called from another Python module if the project exposes one.

The model and feature extractor must use the same feature names, ordering, and preprocessing as the training pipeline.

---

## 🌐 Launching the Web Application

If the Flask entry point is `app.py`, run:

\`\`\`powershell
python app.py
\`\`\`

If the application uses Flask's default development configuration, open:

**http://127.0.0.1:5000/**

Keep the terminal open while using the application. If the configured port differs, use the address printed by Flask.

Use Flask's development server for local development only. Production deployments should use an appropriate production WSGI server.

---

## 🔌 REST API

If the application implements the `/api/predict` endpoint, it may accept JSON requests for URL classification.

| Property | Example |
|---|---|
| Method | `POST` |
| Endpoint | `/api/predict` |
| Content-Type | `application/json` |
| Request field | `url` |

### Example Request

\`\`\`json
{
  "url": "https://example.com/login"
}
\`\`\`

### PowerShell Request Example

\`\`\`powershell
$body = @{
    url = "https://example.com/login"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/api/predict" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
\`\`\`

### Example Response Schema

The following response is illustrative only. Actual fields and values must match the implemented API.

\`\`\`json
{
  "url": "https://example.com/login",
  "is_phishing": false,
  "confidence": 0.82,
  "issues": []
}
\`\`\`

The example classification and confidence are not actual model results.

### API Error Handling

A robust API should handle:

- Missing URL values.
- Invalid JSON.
- Invalid URL formats.
- Missing or incompatible model artifacts.
- Feature extraction errors.
- Unexpected prediction failures.

Return appropriate HTTP status codes and avoid exposing stack traces or internal filesystem paths to clients.

---

## 🧪 Feature Engineering

The following are examples of features commonly used in URL classification. Confirm the actual feature set in the implementation.

| Feature | Category | Purpose |
|---|---|---|
| `url_length` | Lexical | Measures URL character length |
| `has_ip_address` | Structural | Detects IP-address hosts |
| `is_https` | Protocol | Identifies HTTPS usage |
| `is_shortened` | Obfuscation | Detects configured URL-shortening domains |
| `keyword_hits` | Lexical | Counts configured suspicious keywords |
| `suspicious_tld` | Domain structure | Flags configured top-level domains |
| `num_subdomains` | Structural | Measures subdomain depth |
| `entropy` | Statistical | Measures character-distribution randomness |

### Important Considerations

- HTTPS does not guarantee that a website is legitimate.
- A long URL or unusual top-level domain is not sufficient evidence of phishing.
- Feature extraction must remain consistent between training and prediction.
- Heuristic warnings should be distinguished from model-generated predictions.
- External domain lookups require appropriate error handling and may return incomplete or stale information.

---

## 🧫 Testing

If pytest tests are available under `tests/`, run:

\`\`\`powershell
python -m pytest tests/ -v
\`\`\`

Run a specific test file:

\`\`\`powershell
python -m pytest tests/test_pipeline.py -v
\`\`\`

If pytest is missing and is not included in `requirements.txt`:

\`\`\`powershell
python -m pip install pytest
\`\`\`

### Recommended Test Coverage

- URL input validation.
- Feature extraction for valid and malformed URLs.
- Consistency between training and inference features.
- Model loading and prediction.
- API success and error responses.
- Missing model and dataset handling.
- Empty input and malformed JSON.
- Representative phishing and legitimate URL samples.

---

## 🔒 Security Considerations

- **Treat predictions as advisory:** Do not rely on the model as the sole security control.
- **Avoid opening suspicious URLs automatically:** Analyze URL strings without navigating to potentially malicious destinations.
- **Prevent unsafe external requests:** If the application performs reputation lookups, validate destinations and defend against server-side request forgery (SSRF).
- **Protect API endpoints:** Apply input validation, sensible request limits, rate limiting, and access controls where needed.
- **Protect secrets:** Store credentials and sensitive configuration outside public source files.
- **Use secure deployment settings:** Do not expose Flask's development server as a production service.
- **Protect model artifacts:** Load pickle-based serialized models only from trusted sources because deserialization can execute code.
- **Handle scan logs carefully:** Avoid storing sensitive URL parameters or private information unnecessarily.

---

## ⚠️ Limitations

- Classification performance depends on dataset quality, diversity, and label accuracy.
- Newly created phishing campaigns may evade models trained on older data.
- URL-based analysis does not necessarily inspect page content, JavaScript behavior, redirects, or visual impersonation.
- Legitimate websites can exhibit suspicious-looking URL patterns.
- Phishing websites can use HTTPS.
- Prediction confidence is not necessarily a calibrated probability of maliciousness.
- External domain lookups can fail, become unavailable, or return stale information.
- Static GitHub Pages hosting cannot run the Python model or Flask backend.

---

## 🛠️ Troubleshooting

| Problem | Possible Cause | Solution |
|---|---|---|
| `ModuleNotFoundError` | Missing dependency or incorrect Python environment | Activate `.venv` and install `requirements.txt` |
| Dataset not found | Missing file or incorrect path | Verify the configured dataset path |
| Model file not found | Model has not been trained or path differs | Run the training script and verify the model output path |
| Feature dimension mismatch | Training and inference use different features | Use the same preprocessing and feature ordering |
| Flask startup error | Missing dependency or configuration issue | Inspect the terminal traceback |
| Port already in use | Another process is using the port | Stop that process or configure another port |
| API returns 404 | Endpoint path differs | Inspect the Flask route definitions |
| API returns 400 | Invalid request body or URL | Send valid JSON with the required field |
| Unexpected classification | Dataset imbalance, limited features, or model limitations | Evaluate precision, recall, and representative test samples |
| GitHub Actions fails | Dependency or test configuration mismatch | Review workflow logs and reproduce the failing test locally |
| GitHub Pages loads but predictions fail | Backend is unavailable or not configured | Deploy the backend and verify frontend API configuration |

---

## 🚀 Deployment

### GitHub Pages — Frontend

The published project website is available at:

**[https://dhananjaychaudhary99.github.io/Phishing-Website-Detector/](https://dhananjaychaudhary99.github.io/Phishing-Website-Detector/)**

GitHub Pages hosts compatible static assets such as HTML, CSS, and JavaScript. It does not execute Flask or Python machine learning code.

### Flask Backend

For online predictions, deploy the Flask backend to a Python-compatible hosting service and configure the frontend to call the backend's public HTTPS endpoint.

Before deploying, verify that:

- The model and preprocessing artifacts are available.
- The production server starts correctly.
- API input validation and error handling work.
- CORS permits only intended frontend origins, where applicable.
- Secrets and configuration are managed securely.
- The frontend can successfully reach the backend.

No backend hosting provider or backend deployment URL is specified because it has not been confirmed.

---

## 🔮 Future Improvements

- Integrate trusted URL reputation sources with appropriate rate limits and licensing.
- Evaluate regularly updated phishing and legitimate URL datasets.
- Compare Random Forest with other suitable classification algorithms.
- Add model explainability without treating correlations as proof of maliciousness.
- Develop an optional browser extension for suspicious-link warnings.
- Add scan history with privacy controls and retention limits.
- Improve production logging, monitoring, and deployment automation.
- Monitor false positives, false negatives, and model performance drift.
- Add security testing for input validation and unsafe URL handling.

---

## 👨‍💻 Author

**Dhananjay Chaudhary**

- **GitHub:** [@dhananjaychaudhary99](https://github.com/dhananjaychaudhary99)
- **Portfolio:** [Personal Portfolio](https://dhananjaychaudhary99.github.io/Portfolio/)
- **Project Repository:** [Phishing Website Detector](https://github.com/dhananjaychaudhary99/Phishing-Website-Detector)

---

## 📜 License

The project's license should match the `LICENSE` file in the repository. If no license has been added, select and include an appropriate license before claiming specific open-source reuse permissions.

---

## 🙏 Acknowledgments

Built with Python, Flask, and scikit-learn to explore machine-learning-assisted phishing URL classification and defensive cybersecurity analysis.

---

**Disclaimer:** This project is intended for educational and defensive cybersecurity purposes. It does not guarantee detection of every phishing URL and should not replace established security controls.
'@