import cv2 as cv
import numpy as np


class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        # load the image we're trying to match
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

        # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find(self, haystack_img, threshold=0.5):
                
        # create matchTemplate
        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)

        # get coordinates and confidence
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if max_val >= threshold:
            # detection box size
            top_left = max_loc
            bottom_right = (top_left[0] + self.needle_w, top_left[1] + self.needle_h)
            
            # draw detection box
            cv.rectangle(haystack_img, top_left, bottom_right, 
                        color=(0,255,0), 
                        thickness=2,
                        lineType=cv.LINE_4)
            
            cv.imshow('Matches', haystack_img)
            
        return (self.needle_w/2,self.needle_h/2)