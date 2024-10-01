import requests

url = "ldkdnkdd" + ".google.com"
try:
    get_request = requests.get("http://" + url)
    print(get_request)
except requests.exceptions.ConnectionError as e:
    print(e)
    pass