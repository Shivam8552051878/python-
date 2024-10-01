import requests
import re


def extracting_links_from(response):
    response_content = response.content
    return re.findall(r'(?:href=")(.*?)"', response_content.decode())


all_links = []
target_url = "https://zsecurity.org"

def crawler(url):
    get_response = requests.get(url)
    get_link = extracting_links_from(get_response)
    for link in get_link:
        if "https://" not in link:
            link = rf"{url}{link}"
    
        if "#" in link:
            link = link.split("#")[0]
        if url in link and link not in all_links:
            all_links.append(link)
            print(link)
            crawler(link)

crawler(target_url)