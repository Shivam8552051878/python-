import requests

url = "https://www.testyou.in/Login.aspx"
data = {"ctl00$CPHContainer$txtUserLogin":"13", "ctl00$CPHContainer$txtPassword":"123", "ctl00$CPHContainer$btnLoginn":"submit"}
response = requests.post(url, data=data)
print(response.content.decode())