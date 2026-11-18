import time
import urllib.request

print("===== INTERNET CHECKER =====")

url = "https://www.google.com"

try:
    start = time.time()

    response = urllib.request.urlopen(url, timeout=10)

    end = time.time()

    print("Internet Status: Connected")
    print("Website Status:", response.status)
    print("Response Time:", round((end - start) * 1000, 2), "ms")

except Exception:
    print("Internet Status: Not Connected")