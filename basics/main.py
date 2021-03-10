import cv2 as cv
import numpy as np
import os
from time import time, sleep
from wincap import WindowCapture
from vision import Vision
import pyautogui
from threading import Thread

# global flag
is_bot_running = False

def bot_action(result):
    print("New Action for ", result[4])
    
    for i in range(5,0,-1):
        print("\t starts in {}".format(i))
        sleep(1)
    
    target = (result[0], result[1])
    target = wincap.get_screen_position(target)
    pyautogui.click(x=target[0], y=target[1])
    
    global is_bot_running
    is_bot_running = False
    

# Change the working directory to the folder this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
wincap = WindowCapture("BlueStacks")

# initialize the Vision class
vision_start_game = Vision()

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # detect key states
    result = vision_start_game.find(screenshot, 0.95)

    # show detection images
    cv.imshow("Matches", result[2])
            
    # click if necessary
    if not is_bot_running and result[3]:
        is_bot_running = True
        t = Thread(target=bot_action, args=(result,))
        t.start()
    
    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print("Finish.")