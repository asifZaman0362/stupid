import pyautogui
import keyboard
import time


def send_message(clipboard=True, mssg=""):
	if clipboard:
		pyautogui.hotkey("ctrlleft","v")
		pyautogui.hotkey("return")



def start():
	t = 0
	while True:
		time.sleep(0.01)
		if keyboard.is_pressed("p"):
			break;
	while(True):
		time.sleep(0.01)
		t += 1
		if t % 10 == 0:
			send_message()
		if keyboard.is_pressed("q"):
			break


start()