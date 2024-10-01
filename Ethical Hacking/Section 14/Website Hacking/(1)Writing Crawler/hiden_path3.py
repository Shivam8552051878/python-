import requests


def request(url):
    try:
        get_request = requests.get("http://" + url )
        return get_request
    except requests.exceptions.ConnectionError as e:
        pass
    except Exception as e:
        print(e)
        pass


with open("files-and-dirs-wordlist.txt", "r") as file:
    word_list = file.read().split()

hiden_path = []
target_url = "google.com"
for words in word_list:
    url = f"{target_url}\words"
    response = request(url)
    if response:
        hiden_path.append(word_list)
        print(f"[+]Discover Url --> https://{url}")

print(hiden_path)