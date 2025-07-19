import requests

# Tor proxy
proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

def tor_request(url):
    try:
        response = requests.get(url, proxies=proxies, timeout=20)
        return response.text
    except Exception as e:
        print("Tor Connection Failed:", e)
        return None

if __name__ == "__main__":
    print("Connecting to onion...")
    html = tor_request("http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion")
    if html:
        print("Connected Successfully\n", html[:300])
