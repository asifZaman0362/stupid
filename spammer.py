import pyautogui
import keyboard
import time


def send_message(clipboard=True, mssg=""):
	if clipboard:
		pyautogui.hotkey("ctrlleft","v")
		pyautogui.hotkey("return")
	else:
		# whatever



def start():
	while True:
		time.sleep(0.01)
		if keyboard.is_pressed("p"):
			break;
	while(True):
		time.sleep(0.2)
		send_message()
		if keyboard.is_pressed("p"):
			break


start()