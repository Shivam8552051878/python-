import requests


def request(url):
    try:
        get_request = requests.get("https://" + url )
        return get_request
    except requests.exceptions.ConnectionError as e:
        pass
    except Exception as e:
        print(e)
        pass


target_url = "google.com"
response = request(target_url)
print(response.content)