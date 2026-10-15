Set-Content -Path "README.md" -Encoding utf8 -Value @'
# Phishing Website Detector — ML-Based URL Classification

A machine learning-based cybersecurity application that analyzes URLs and classifies them as potentially legitimate or phishing using lexical, structural, and statistical URL features. Built with **Python, Flask, and a Random Forest classifier**, the project provides a web dashboard, command-line predictions, heuristic security diagnostics, and a REST API.

The application is designed as a defensive analysis tool to help identify suspicious links. Predictions are advisory and do not guarantee that a website is safe or malicious.

---

## Table of Contents

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

## Overview

Phishing attacks use deceptive URLs and websites to trick users into revealing passwords, financial information, and other sensitive data. This project explores how machine learning and URL-based feature engineering can help detect suspicious links.

The system extracts configured URL characteristics, transforms them into a feature representation, and passes the resulting data to a trained classification model. The application can present the prediction alongside heuristic warnings when those diagnostics are implemented.

### Project Objectives

- Identify potentially suspicious URLs through automated classification.
- Apply machine learning to lexical and structural URL characteristics.
- Provide interpretable security indicators alongside classification results.
- Support predictions through a web interface, command-line interface, and REST API.
- Separate feature extraction, model training, inference, and presentation logic.
- Support repeatable development and testing workflows.

---

## Key Features

- **URL Feature Extraction:** Analyzes configured characteristics such as URL length, IP-address usage, subdomain structure, and suspicious keywords.
- **Machine Learning Classification:** Uses a Random Forest classifier trained on labeled URL data.
- **Security Diagnostics:** Provides heuristic warnings for configured suspicious URL patterns.
- **Flask Web Dashboard:** Offers a browser-based interface for URL analysis.
- **Command-Line Predictions:** Supports URL classification from the terminal.
- **REST API:** Enables JSON-based integration with other applications.
- **Model Persistence:** Saves the trained model for reuse during inference.
- **Data Processing:** Supports dataset preparation and feature extraction.
- **Automated Testing:** Uses pytest for regression testing.
- **Modular Architecture:** Separates the web application, model, training pipeline, and feature extraction logic.

> Feature availability depends on the actual implementation and configuration in the repository.

---

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python 3.10+ |
| Web Framework | Flask |
| Machine Learning | scikit-learn |
| Classification Algorithm | Random Forest |
| Data Processing | pandas, NumPy |
| Domain Parsing | tldextract |
| Model Persistence | joblib |
| Domain Registration Lookup | python-whois, if implemented |
| Database | SQLite, if scan logging is implemented |
| Testing | pytest |
| Version Control | Git and GitHub |
| Continuous Integration | GitHub Actions, if configured |

---

## Project Structure

```text
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
```

### Important Files

| File | Responsibility |
|---|---|
| `app.py` | Flask routes, web interface, and API endpoints |
| `requirements.txt` | Python dependency definitions |
| `src/feature_extraction.py` | Extracts features from URLs |
| `src/train.py` | Prepares data, trains the model, and saves the artifact |
| `src/predict.py` | Provides command-line and programmatic inference |
| `models/phishing_model.pkl` | Serialized trained model |
| `data/raw/dataset.csv` | Source dataset containing labeled URLs |
| `data/processed/cleaned_data.csv` | Processed dataset, if generated by the training pipeline |
| `templates/index.html` | HTML dashboard template |
| `static/css/style.css` | Dashboard styling |
| `static/js/main.js` | Frontend interactions |
| `tests/test_pipeline.py` | Automated tests |
| `scans.db` | SQLite scan records, if used by the application |
| `.github/workflows/test.yml` | Continuous integration workflow |

**Note:** This is the intended project layout. Files that are not present in your repository should be created only if required by the implementation.

---

## System Architecture

```text
                 ┌───────────────────────┐
                 │       User Input      │
                 │    Web / CLI / API    │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │    Input Validation   │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   Feature Extraction  │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Trained Random Forest │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │  Classification Result│
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Result and Diagnostics│
                 └───────────────────────┘
```

### Processing Pipeline

1. Receive a URL through the dashboard, CLI, or API.
2. Validate the input and normalize it consistently with the training pipeline.
3. Extract the features expected by the trained model.
4. Generate a classification using the saved model.
5. Evaluate configured heuristic checks, if available.
6. Return the prediction and applicable diagnostics to the user.

---

## Installation and Setup

### Prerequisites

Install Python 3.10 or later and Git.

Verify the installations in PowerShell:

```powershell
python --version
python -m pip --version
git --version
```

### 1. Clone the Repository

```powershell
git clone https://github.com/dhananjaychaudhary99/Phishing-Website-Detector.git
Set-Location Phishing-Website-Detector
```

### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate the Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, allow scripts for the current terminal session only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Verify the Project Files

```powershell
Get-ChildItem
Get-ChildItem src
Get-ChildItem models
```

Check that the source dataset and trained model exist before running commands that depend on them.

---

## Training the Model

Run the training script from the project root:

```powershell
python src\train.py
```

The expected training workflow is:

1. Load the labeled URL dataset.
2. Validate and prepare the data.
3. Extract features using the project's feature extraction implementation.
4. Split the dataset into training and testing sets.
5. Train the Random Forest classifier.
6. Evaluate the model on held-out data.
7. Save the trained model to the configured output path.

Expected paths, subject to the actual training configuration:

```text
data/raw/dataset.csv
data/processed/cleaned_data.csv
models/phishing_model.pkl
```

### Model Evaluation

Useful evaluation metrics include:

| Metric | Purpose |
|---|---|
| Accuracy | Overall proportion of correct predictions |
| Precision | Proportion of predicted phishing URLs that are actually phishing |
| Recall | Proportion of phishing URLs correctly identified |
| F1-score | Harmonic mean of precision and recall |
| Confusion Matrix | Shows false positives, false negatives, and correct classifications |

For phishing detection, evaluate false negatives and false positives carefully. A high accuracy score alone does not establish that the model is reliable.

---

## Making Predictions

### Command-Line Interface

If `src/predict.py` accepts a URL as a positional argument, use:

```powershell
python src\predict.py "http://example.com/login"
```

Replace the example URL with the URL you want to analyze.

If the script expects different arguments, use the interface implemented in `src/predict.py`.

### Python Integration

A reusable prediction function can be called from another Python module if the project exposes an appropriate function.

The model and feature extractor must use the same feature names, ordering, and preprocessing as the training pipeline.

---

## Launching the Web Application

Start the Flask application:

```powershell
python app.py
```

If the application uses Flask's default development configuration, open:

**http://127.0.0.1:5000**

Keep the terminal open while using the application.

If the project configures a different port, use the address printed by Flask.

---

## REST API

If the Flask application implements the `/api/predict` endpoint, it can accept JSON requests for URL classification.

| Property | Value |
|---|---|
| Method | `POST` |
| Endpoint | `/api/predict` |
| Content-Type | `application/json` |
| Request field | `url` |

### Example Request

```json
{
  "url": "http://example.com/login"
}
```

### PowerShell Request Example

```powershell
$body = @{
    url = "http://example.com/login"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://127.0.0.1:5000/api/predict" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

### Example Response Schema

The following illustrates a possible response format. Actual field names and values must match the implementation.

```json
{
  "url": "http://example.com/login",
  "is_phishing": false,
  "confidence": 0.82,
  "issues": [],
  "features": {
    "url_length": 23,
    "has_ip_address": 0,
    "is_https": 0
  }
}
```

The example prediction is illustrative, not an actual model result.

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

## Feature Engineering

The following table describes common URL features that may be used by this type of classifier. Confirm the exact feature set in `src/feature_extraction.py`.

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
- Features based on domain registration or external reputation require additional lookups and appropriate error handling.

---

## Testing

Run the test suite from the project root:

```powershell
python -m pytest tests/ -v
```

Run a specific test file:

```powershell
python -m pytest tests/test_pipeline.py -v
```

If pytest is not installed and is not included in `requirements.txt`:

```powershell
python -m pip install pytest
```

### Recommended Test Coverage

- URL input validation.
- Feature extraction for valid and malformed URLs.
- Consistency between training and inference features.
- Model loading and prediction.
- API success and error responses.
- Missing model and dataset handling.
- Empty input and malformed JSON.
- Classification behavior on representative test samples.

---

## Security Considerations

- **Treat predictions as advisory:** Never rely on the model as the sole security control.
- **Do not automatically open suspicious URLs:** Analyze URL strings without navigating to potentially malicious destinations.
- **Avoid unsafe external requests:** If reputation checks or domain lookups are added, validate destinations and defend against server-side request forgery (SSRF).
- **Protect API endpoints:** Apply request validation, sensible size limits, rate limiting, and appropriate access controls where needed.
- **Keep secrets out of source control:** Store credentials and configuration secrets in environment variables or a dedicated secret manager.
- **Use safe deployment settings:** Do not expose Flask's development server as a production service. Use a production WSGI server, appropriate HTTPS termination, and secure configuration.
- **Protect model artifacts:** Load serialized models only from trusted sources because pickle-based artifacts can execute code during deserialization.
- **Handle scan logs carefully:** Avoid storing sensitive query parameters or other private URL data unnecessarily.

---

## Limitations

- Classification performance depends on dataset quality, diversity, and label accuracy.
- New phishing campaigns may evade models trained on older data.
- Lexical analysis does not necessarily inspect webpage content, JavaScript behavior, redirects, or visual impersonation.
- Benign websites can contain suspicious-looking URL patterns.
- Phishing websites can use HTTPS and otherwise appear technically valid.
- Prediction confidence is not necessarily a calibrated probability of a URL being malicious.
- External domain lookups may fail, become unavailable, or return stale information.

---

## Troubleshooting

| Problem | Possible Cause | Solution |
|---|---|---|
| `ModuleNotFoundError` | Dependencies are missing or the wrong Python environment is active | Activate `.venv` and install `requirements.txt` |
| `FileNotFoundError` for the dataset | Dataset path is incorrect or the file is missing | Verify `data/raw/dataset.csv` |
| Model file not found | Training has not completed or the output path differs | Run the training script and verify the configured model path |
| Feature dimension mismatch | Training and inference use different features | Use the same feature extraction pipeline and feature ordering |
| Flask import or startup error | Missing dependency or configuration problem | Inspect the traceback and install required dependencies |
| Port 5000 is already in use | Another process is using the port | Stop the relevant process or configure another port |
| API returns 404 | Endpoint is missing or the route differs | Inspect the Flask route definitions in `app.py` |
| API returns 400 | Request body or URL input is invalid | Send valid JSON with the required `url` field |
| Unexpected classification | Dataset imbalance, poor features, or model limitations | Evaluate precision, recall, and representative test samples |
| GitHub Actions fails | Dependency, environment, or test configuration mismatch | Review the workflow logs and reproduce the failing test locally |

---

## Future Improvements

- **Threat Intelligence:** Integrate trusted URL reputation feeds with appropriate rate limits and licensing.
- **Improved Datasets:** Evaluate regularly updated, deduplicated phishing and legitimate URL datasets.
- **Model Comparison:** Compare Random Forest with other suitable classification approaches.
- **Explainability:** Report meaningful feature contributions without presenting heuristic correlations as proof.
- **Browser Extension:** Add optional warnings when users encounter suspicious links.
- **Database Integration:** Store scan history with retention controls and appropriate privacy protections.
- **Production Deployment:** Add structured logging, monitoring, configuration management, and automated deployment.
- **Continuous Evaluation:** Monitor false positives, false negatives, and model performance drift.
- **Security Testing:** Add validation, dependency scanning, and tests for unsafe URL handling.

---

## Author

**Dhananjay Chaudhary**

- **GitHub:** [@dhananjaychaudhary99](https://github.com/dhananjaychaudhary99)
- **Portfolio:** [dhananjaychaudhary99.github.io/Portfolio](https://dhananjaychaudhary99.github.io/Portfolio/)
- **Project Repository:** [Phishing Website Detector](https://github.com/dhananjaychaudhary99/Phishing-Website-Detector)

---

## License

This project is intended to use the MIT License. Review the repository's `LICENSE` file to confirm the actual license and applicable terms.

---

## Acknowledgments

Built with Python, Flask, and scikit-learn to explore machine-learning-assisted phishing URL classification and defensive cybersecurity analysis.

---

**Disclaimer:** This project is intended for educational and defensive security purposes. It does not guarantee detection of every phishing URL and should not replace established security controls.
'@