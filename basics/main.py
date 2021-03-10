import cv2 as cv
import numpy as np
import os
from time import time
from wincap import WindowCapture
from vision import Vision

# Change the working directory to the folder this script is in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize the WindowCapture class
wincap = WindowCapture('BlueStacks')

# initialize the Vision class
vision_start_game = Vision('../images/start_game.JPG')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_start_game.find(screenshot, 0.95)

    cv.imshow('Matches', points[2])

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')