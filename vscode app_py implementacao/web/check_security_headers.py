# web/check_security_headers.py
import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_security_headers(url):
    try:
        r = requests.get(url, timeout=10)
    except Exception as e:
        print("Erro ao conectar:", e)
        return

    print(f"HTTP status: {r.status_code}")
    headers = r.headers
    for h in SECURITY_HEADERS:
        if h in headers:
            print(f"[OK] {h}: {headers[h]}")
        else:
            print(f"[MISSING] {h}")
    # Checar cookies inseguros
    cookies = r.cookies
    if cookies:
        print("Cookies recebidos (examine flags Secure/HttpOnly):")
        # requests hides some flags; para inspeção aprofundada, usar Burp/OWASP ZAP ou manualmente inspecionar Set-Cookie header
        if "Set-Cookie" in headers:
            print(headers["Set-Cookie"])
    else:
        print("Nenhum cookie recebido.")
