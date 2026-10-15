import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from feature_extraction import extract_features
from predict import predict_url

def test_extract_features():
    feats = extract_features("https://www.google.com")
    assert isinstance(feats, dict)
    assert feats["is_https"] == 1
    assert feats["has_ip_address"] == 0

def test_predict_url():
    res = predict_url("http://192.168.1.1/login-verify")
    assert "is_phishing" in res
    assert "confidence" in res
    assert isinstance(res["is_phishing"], bool)
