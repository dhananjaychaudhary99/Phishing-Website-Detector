import re
import math
from urllib.parse import urlparse
import tldextract
import pandas as pd

SUSPICIOUS_KEYWORDS = [
    'login', 'verify', 'update', 'secure', 'banking', 'account',
    'signin', 'password', 'confirm', 'wallet', 'auth', 'support',
    'security', 'authenticate', 'billing', 'ebay', 'paypal', 'service'
]

SHORTENERS = [
    'bit.ly', 'goo.gl', 'tinyurl.com', 'ow.ly', 't.co', 
    'is.gd', 'buff.ly', 'adf.ly', 'tiny.cc'
]

SUSPICIOUS_TLDS = {'xyz', 'top', 'tk', 'ml', 'ga', 'cf', 'gq', 'ru', 'work', 'date', 'racing', 'loan'}

def calculate_entropy(text: str) -> float:
    if not text:
        return 0.0
    prob = [float(text.count(c)) / len(text) for c in set(text)]
    return -sum(p * math.log2(p) for p in prob)

def is_private_ip(hostname: str) -> bool:
    private_patterns = [
        r'^127\.', r'^10\.', r'^192\.168\.', r'^172\.(1[6-9]|2[0-9]|3[0-1])\.', r'^localhost$'
    ]
    return any(re.match(pattern, hostname) for pattern in private_patterns)

def extract_features(url: str) -> dict:
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    parsed = urlparse(url)
    ext = tldextract.extract(url)
    hostname = (parsed.netloc or "").lower().split(':')[0]
    path = (parsed.path or "").lower()
    full_url = url.lower()

    ip_regex = r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-5])'
    has_ip = 1 if re.search(ip_regex, hostname) else 0

    # If it is a local/private network IP, don't flag as malicious external IP
    if is_private_ip(hostname):
        has_ip = 0

    is_shortened = 1 if any(shortener in hostname for shortener in SHORTENERS) else 0
    subdomains = ext.subdomain.split('.') if ext.subdomain else []
    num_subdomains = len([s for s in subdomains if s])
    keyword_hits = sum(1 for kw in SUSPICIOUS_KEYWORDS if kw in full_url)
    has_suspicious_tld = 1 if ext.suffix in SUSPICIOUS_TLDS else 0
    digit_count = sum(c.isdigit() for c in url)

    return {
        'url_length': len(url),
        'hostname_length': len(hostname),
        'path_length': len(path),
        'has_ip_address': has_ip,
        'is_shortened': is_shortened,
        'count_dots': url.count('.'),
        'count_hyphens': url.count('-'),
        'count_at': url.count('@'),
        'count_question': url.count('?'),
        'count_percent': url.count('%'),
        'count_equal': url.count('='),
        'count_slash': url.count('/'),
        'count_digits': digit_count,
        'entropy': round(calculate_entropy(url), 4),
        'is_https': 1 if parsed.scheme == 'https' else 0,
        'num_subdomains': num_subdomains,
        'keyword_hits': keyword_hits,
        'suspicious_tld': has_suspicious_tld
    }

def extract_dataframe(urls: list) -> pd.DataFrame:
    return pd.DataFrame([extract_features(u) for u in urls])
