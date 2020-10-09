import requests
import keyboard
from PIL import ImageGrab
import io
import pyautogui

phase = 0
start = (0,0)
end = (0,0)

token = ""

with open("token.txt") as f:
	token = f.read()


def onpress(event):
    global phase
    global start
    global end
    if phase == 0:
        start = pyautogui.position()
        print("[Point] Start Point selected")
    elif phase == 1:
        end = pyautogui.position()
        print("[Point] End Point selected")

        print("[Screengrab] Grabbing Screen...")
        img = ImageGrab.grab((start[0], start[1], end[0], end[1]))
        buffer = io.BytesIO()
        print("[Screengrab] Saving to buffer...")
        img.save(buffer, format="PNG")

        print("[Request] Sending to server...")
        r = requests.post("https://api.ocr.space/parse/image", data={ "apikey": token },
        files={ "filename": ("scr.png", buffer.getvalue()) })
        try:
            print("[Text] "+r.json()["ParsedResults"][0]["ParsedText"])
        except:
            print("[Error] "+r.text)
            pass




    phase += 1
keyboard.on_press_key("r", onpress)
while phase != 2:
    pass
input("")

