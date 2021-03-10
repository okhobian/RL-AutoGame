import cv2 as cv
import numpy as np

# load images
haystack_img = cv.imread('../images/example_main_menu.JPG', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('../images/start_game.JPG', cv.IMREAD_UNCHANGED)

# create matchTemplate
result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

# get coordinates and confidence
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

# set thershold to 80%
threshold = 0.8
if max_val >= threshold:
    
    # needle_img shape
    needle_img_w = needle_img.shape[1]
    needle_img_h = needle_img.shape[0]
    
    # detection box size
    top_left = max_loc
    bottom_right = (top_left[0] + needle_img_w, top_left[1] + needle_img_h)
    
    # draw detection box
    cv.rectangle(haystack_img, top_left, bottom_right, 
                 color=(0,255,0), 
                 thickness=2,
                 lineType=cv.LINE_4)
    
    # show detected img
    cv.imshow('Result', haystack_img)
    cv.waitKey()
    
else:
    print('not found')