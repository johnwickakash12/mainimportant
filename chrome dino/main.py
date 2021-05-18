import pyautogui
from PIL import Image,ImageGrab
import time
def hit(key):
    pyautogui.keyDown(key)
    return
# def takescreenshot():
    # image=ImageGrab.grab()
    
    # return image
def iscollide(data):
    for i in range(350,430):
        for j in range(540,560):
            if data[i,j]<100:
                hit("down")
                time.sleep(0.2)
                hit("up")
                return
    for i in range(470,500):
        for j in range(620,680):
            if data[i ,j]<100:
                hit("up") 
                return  
                
    return False


if __name__ == '__main__':
    print("starting dino game")
    # takescreenshot()
    time.sleep(3)
    while True:
        imag=ImageGrab.grab().convert('L')
        data=imag.load()
        iscollide(data)
            
            
        # for i in range(350,430):
        #     for j in range(540,560):
        #         data[i ,j]=1
        # for i in range(470,500):
        #     for j in range(620,680):
        #      data[i,j]=1
                
        # imag.show()
        # break
    
   