import requests, random

host_list = [
    b"google.com",
    b"amazon.com",
    b"facebook.com",
    b"youtube.com",
    b"twitter.com",
    b"wikipedia.org",
    b"instagram.com",
    b"linkedin.com",
    b"reddit.com"
]

def fetch_all_chrome_versions():
    versions = []
    url = "https://versionhistory.googleapis.com/v1/chrome/platforms/win/channels/stable/versions"
    while True:
        data = requests.get(url).json()
        versions.extend(v["version"] for v in data.get("versions", []))
        token = data.get("nextPageToken")
        if not token:
            break
        url = f"https://versionhistory.googleapis.com/v1/chrome/platforms/win/channels/stable/versions?pageToken={token}"
    return versions

api_versions = fetch_all_chrome_versions()

def user_agent_generator() -> bytes:
    chrome_version = random.choice(api_versions)
    os_version = random.choice(["6.1", "6.3", "10.0"])
    arch = random.choice(["Win64; x64", "WOW64"])
    ua = f"Mozilla/5.0 (Windows NT {os_version}; {arch}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"
    return ua.encode()

def generate_payload(host: bytes, path: bytes) -> bytes:
    buffer = b""
    buffer += b"GET " + path + b" HTTP/1.1\r\n"
    buffer += b"Host: " + host + b"\r\n"
    buffer += b"Connection: keep-alive\r\n"
    buffer += b"Upgrade-Insecure-Requests: 1\r\n"
    buffer += b"User-Agent: " + user_agent_generator() + b"\r\n"
    buffer += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8\r\n"
    buffer += b"Accept-Encoding: gzip, deflate\r\n"
    buffer += b"Accept-Language: en-US,en;q=0.9\r\n"
    buffer += b"Sec-Fetch-Site: none\r\n"
    buffer += b"Sec-Fetch-Mode: navigate\r\n"
    buffer += b"Sec-Fetch-User: ?1\r\n"
    buffer += b"Sec-Fetch-Dest: document\r\n"
    buffer += b"\r\n"
    return buffer
