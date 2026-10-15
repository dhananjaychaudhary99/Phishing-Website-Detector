import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from feature_extraction import extract_features
from predict import predict_url

def test_feature_extraction():
    feats = extract_features("https://www.google.com")
    assert isinstance(feats, dict)
    assert feats["is_https"] == 1
    assert feats["count_dots"] == 2

def test_prediction():
    res = predict_url("http://192.168.1.1/update-login")
    assert "is_phishing" in res
    assert "confidence" in res
    assert isinstance(res["is_phishing"], bool)
