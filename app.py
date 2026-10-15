import os
import sys
import sqlite3
from datetime import datetime
from urllib.parse import urlparse
import whois
from flask import Flask, render_template, request, jsonify

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from predict import predict_url

app = Flask(__name__, static_folder="static", template_folder="templates")
DB_PATH = "scans.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            is_phishing INTEGER NOT NULL,
            confidence REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

def check_domain_age(url):
    try:
        parsed = urlparse(url if url.startswith(('http://', 'https://')) else 'http://' + url)
        domain = parsed.netloc.split(':')[0]
        if domain.replace('.', '').isdigit() or 'localhost' in domain:
            return None, "Internal Network (No WHOIS)"

        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:
            age_days = (datetime.now() - creation_date).days
            return age_days, f"{age_days} days old"
        return None, "Creation Date Private"
    except Exception:
        return None, "WHOIS Not Reachable"

def detect_problems(features, domain_age_days):
    problems = []
    if features.get('is_https') == 0:
        problems.append("Insecure Connection: Uses plain unencrypted HTTP without SSL certificate.")
    if features.get('has_ip_address') == 1:
        problems.append("Direct IP Host: Exposes direct IP format to conceal identity.")
    if features.get('is_shortened') == 1:
        problems.append("Obfuscated Link: Uses shortener to mask target destination.")
    if features.get('keyword_hits', 0) > 0:
        problems.append(f"Targeting Keywords: Found {features['keyword_hits']} authentication/credential targeting tokens.")
    if features.get('num_subdomains', 0) > 2:
        problems.append(f"Excessive Subdomains: {features['num_subdomains']} domain levels identified (potential spoofing).")
    if features.get('url_length', 0) > 75:
        problems.append(f"Abnormally Long URL: Payload is {features['url_length']} characters long.")
    if features.get('suspicious_tld') == 1:
        problems.append("High-Risk Domain TLD: Registered on an extension known for spam campaigns.")
    if domain_age_days is not None and domain_age_days < 30:
        problems.append(f"Newly Created Domain: Registered only {domain_age_days} days ago (< 30 days is high threat).")
    return problems

def save_scan(url, is_phishing, confidence):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scans (url, is_phishing, confidence, timestamp) VALUES (?, ?, ?, ?)",
        (url, 1 if is_phishing else 0, confidence, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

def get_recent_scans(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT url, is_phishing, confidence, timestamp FROM scans ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [{"url": r[0], "is_phishing": bool(r[1]), "confidence": r[2], "timestamp": r[3]} for r in rows]

@app.route("/", methods=["GET", "POST"])
def home():
    data = None
    issues = []
    domain_age_text = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if url:
            data = predict_url(url)
            age_days, domain_age_text = check_domain_age(url)
            issues = detect_problems(data.get("features", {}), age_days)
            save_scan(url, data["is_phishing"], data["confidence"])

    recent_scans = get_recent_scans()
    return render_template("index.html", data=data, issues=issues, domain_age_text=domain_age_text, recent_scans=recent_scans)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    payload = request.get_json(force=True, silent=True) or {}
    url = payload.get("url", "").strip()
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    res = predict_url(url)
    age_days, domain_age_text = check_domain_age(url)
    res["domain_age"] = domain_age_text
    res["issues"] = detect_problems(res.get("features", {}), age_days)
    save_scan(url, res["is_phishing"], res["confidence"])
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
