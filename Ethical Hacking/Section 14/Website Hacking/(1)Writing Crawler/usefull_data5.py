import requests
import re

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
response_content = response.content
use_data = re.findall(r'(?:href=")(.*?)"', response_content.decode())
print(len(use_data))
print(use_data)