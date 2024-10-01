import requests


def request(url):
    try:
        get_request = requests.get("http://" + url )
        return get_request
    except requests.exceptions.ConnectionError as e:
        pass


with open("subdomains-wodlist.txt", "r") as file:
    data = file.read().split()

subdomains = []
target_url = "google.com"
for subdomain in data:
    url = f"{subdomain}.{target_url}"
    response = request(url)
    if response:
        subdomains.append(data)
        print(f"[+]Url: https://{url}")

print(subdomains)