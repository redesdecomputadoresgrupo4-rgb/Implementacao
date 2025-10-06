# recon/passive_recon.py
import requests
from urllib.parse import urljoin
import json
import os

def fetch_headers(url):
    try:
        r = requests.get(url, timeout=10, allow_redirects=True)
        return r.status_code, dict(r.headers)
    except Exception as e:
        return None, {"error": str(e)}

def fetch_robots(url):
    robots_url = urljoin(url, "/robots.txt")
    try:
        r = requests.get(robots_url, timeout=5)
        return r.status_code, r.text
    except Exception as e:
        return None, str(e)

def passive_recon(url, outdir="reports"):
    os.makedirs(outdir, exist_ok=True)
    status, headers = fetch_headers(url)
    s2, robots = fetch_robots(url)
    result = {
        "target": url,
        "http_status": status,
        "headers": headers,
        "robots_status": s2,
        "robots": robots
    }
    fname = os.path.join(outdir, "passive_recon.json")
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[+] Resultado salvo em {fname}")
