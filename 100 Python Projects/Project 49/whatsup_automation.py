from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

PATH = "C:/Users/kdlte/Downloads/chromedriver_win32/chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time
from PIL import ImageGrab
import tempfile
import os

# Initialize WebDriver
driver = webdriver.Chrome(executable_path=PATH)

# # Open the first website in the first tab
# driver.get('https://web.whatsapp.com/')
# time.sleep(20)

# Open a new tab
driver.execute_script("window.open('', '_blank');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Open the second website in the new tab
driver.get('https://web.whatsapp.com/send?phone=+918552051878')
time.sleep(40)
photo_path = "C:/Users/kdlte/PycharmProjects/Project 49/goal.png"

try:
    plus_btn = driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div')
    print("step 1")
    plus_btn.click()
    photo_video_option = driver.find_element(by=By.XPATH, value='//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    print("step 1")
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_img:
        im = ImageGrab.grabclipboard()
        if im:
            im.save(temp_img.name, 'PNG')
            photo_video_option.send_keys(temp_img.name)
            time.sleep(3)
            print("step 4")
            # Click the send button
            send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
            send_button.click()
            time.sleep(2)
            os.unlink(temp_img.name)
        else:
            print("Clipboard does not contain a valid image.")
except NoSuchElementException:
    print("Element not found")
except:
    print("Not find")



#In this code snippet, the XPath expression '//input[@type="file"]' is used to locate the file input element based on its type attribute. This is a more general approach that should work as long as the file input element on the WhatsApp Web page has the type attribute set to "file".
#If you continue to experience difficulties, you may need to inspect the WhatsApp Web page's HTML structure further and adjust your XPath expression accordingly.
# Perform actions on the second tab if needed
# Close the second tab
driver.close()
# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
# Close the first tab (optional, depending on your use case)
# driver.close()

# Close WebDriver
driver.quit()
