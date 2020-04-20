from email.message import EmailMessage
from selenium import webdriver
from PIL import Image
import smtplib
import hashlib
import numpy
import time
import os

def compare():
    driver = webdriver.Chrome('chromeDriver v80')
    driver.get('https://drive.google.com/open?id=1A7CT_l_6k5Ke6FioxM-BPazDROybBjOC')
    time.sleep(6)
    screenshot = driver.save_screenshot('mScreenshot.png')
    driver.quit()
    image = Image.open("mScreenshot.png")
    os.system('cmd /c "certutil -hashfile mScreenshot.png SHA256> oldHash.txt"')
    file = open("oldHash.txt")
    hashVal = file.readlines()
    time.sleep(10)
    driver = webdriver.Chrome('chromedriver')
    driver.get('https://drive.google.com/open?id=1A7CT_l_6k5Ke6FioxM-BPazDROybBjOC')
    time.sleep(6)
    newScreenshot = driver.save_screenshot('nScreenshot.png')
    driver.quit()
    newImage = Image.open("nScreenshot.png")
    os.system('cmd /c "certutil -hashfile nScreenshot.png SHA256> newHash.txt"')
    newFile = open("newHash.txt")
    newHashVal = newFile.readlines()
    if hashVal[1] != newHashVal[1]:
        sendMail()
    else:
        print("No change detected!")

def sendMail():
    print("Change detected!")
    print("Initiating SMTP server")
    user = os.environ.get("adminUser")
    passwd = os.environ.get("adminPassword")
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        msg = EmailMessage()
        msg['Subject'] = "Alert! Site has been updated."
        msg['From'] = user
        msg['To'] = 'rushil.rc@gmail.com'
        msg.set_content('Hi Rushil,\nThe content for the site you were added to monitor has been updated. Click here to check: https://drive.google.com/open?id=1A7CT_l_6k5Ke6FioxM-BPazDROybBjOC')
        smtp.login(user,passwd)
        smtp.send_message(msg)
    print ("Done")

compare()
