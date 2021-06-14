import pyautogui,time
time.sleep(3)
f =open("New Text Document.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
