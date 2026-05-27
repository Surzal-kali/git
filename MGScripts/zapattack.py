#here be our first big step to a terminal based altnerative to burp suite :D
import time

from Documents.SurzsEnviro.target_config import ZAP_PASS

ZAP_PROXIES = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}


def _build_zap_client():
    try:
        from zapv2 import ZAPv2
    except ImportError as err:
        raise ImportError(
            "zapattack requires python-owasp-zap-v2.4. Install repo dependencies "
            "with `python3 -m pip install -r requirements.md` from the repo root."
        ) from err

    return ZAPv2(apikey=ZAP_PASS, proxies=ZAP_PROXIES)


def _print_alerts(alerts):
    for alert in alerts:
        print(f"Alert: {alert['alert']} - Risk: {alert['risk']} - URL: {alert['url']}")


def zap_scan(target_url):
    zap = _build_zap_client()
    print(f"[*] Starting ZAP scan on {target_url}")
    zap.urlopen(target_url)
    zap.spider.scan(target_url)
    while int(zap.spider.status()) < 100:
        print(f"[*] Spider progress: {zap.spider.status()}%")
        time.sleep(2)
    print("[*] Spidering completed. Starting active scan...")
    zap.ascan.scan(target_url)
    while int(zap.ascan.status()) < 100:
        print(f"[*] Active scan progress: {zap.ascan.status()}%")
        time.sleep(5)
    print("[*] Active scan completed. Fetching results...")
    _print_alerts(zap.core.alerts(baseurl=target_url))


def zap_passive_scan(target_url):
    zap = _build_zap_client()
    print(f"[*] Starting ZAP passive scan on {target_url}")
    zap.urlopen(target_url)
    print("[*] Passive scan completed. Fetching results...")
    _print_alerts(zap.core.alerts(baseurl=target_url))
