import pyautogui
import keyboard
import pyperclip
import time


def send_message(clipboard=True, mssg=""):
	if clipboard:
		pyautogui.hotkey("ctrlleft","v")
		pyautogui.hotkey("return")


def get_data():
    with open('/home/zero/stupid/data.txt', 'r') as _file:
        line = _file.readline()
        dat = []
        while line:
            dat.append(line)
            line = _file.readline()
    return dat

def start_file_based():
    dat = get_data()
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed("p"):
            break
    for i in dat:
        time.sleep(0.05)
        pyperclip.copy(i)
        pyperclip.paste()
        send_message()
        if keyboard.is_pressed("q"):
            break

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


time.sleep(2)
start_file_based()
