import requests
import re

def extracting_links_from(response):
    response_content = response.content
    return re.findall(r'(?:href=")(.*?)"', response_content.decode())

all_links = []
target_link = "https://zsecurity.org"
get_response = requests.get(target_link)
get_link = extracting_links_from(get_response)
for link in get_link:
    if "https://" not in link:
        link = rf"{target_link}{link}"

    if "#" in link:
        link = link.split("#")
    if target_link in link and link not in all_links:
        all_links.append(link)
        print(link)