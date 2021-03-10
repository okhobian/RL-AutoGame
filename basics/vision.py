import cv2 as cv
import numpy as np
from operator import itemgetter


class Vision:

    needle_img_paths = {
        "start" : "../images/start_game.JPG",
        "reward": "../images/get_reward.JPG",
        "back"  : "../images/back_to_main.JPG"  
    }

    needle_imgs = {
        "start" : None,
        "reward": None,
        "back"  : None  
    }
    
    method = None
    click_flag = False
    click_x = None
    click_y = None

    # constructor
    def __init__(self, method=cv.TM_CCOEFF_NORMED):
        # load the images
        for path in self.needle_img_paths:
            # self.needle_imgs[path] = cv.imread(self.needle_img_paths[path], cv.IMREAD_UNCHANGED)
            self.needle_imgs[path] = cv.imread(self.needle_img_paths[path], cv.IMREAD_GRAYSCALE)

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find(self, haystack_img, threshold=0.5):
        
        self.click_flag = False
        
        # convert haystack to grayscale
        haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)
        
        # results[i] is a tupe: (min_val, max_val, min_loc, max_loc, img_type)
        results = []
        for img in self.needle_imgs:
            results.append( cv.minMaxLoc( cv.matchTemplate(haystack_img, self.needle_imgs[img], self.method) ) + (img,) )
        
        # select one mostlikly needle based on max_val (confidence)
        min_val, max_val, min_loc, max_loc, img_type = max(results,key=itemgetter(1))
        
        # get detected boundry
        needle_w = self.needle_imgs[img_type].shape[1]
        needle_h = self.needle_imgs[img_type].shape[0]

        if max_val >= threshold:
            # detection box size
            bottom_left = max_loc
            top_right = (bottom_left[0] + needle_w, bottom_left[1] + needle_h)
            
            # print(bottom_left, top_right)
            
            # draw detection box
            cv.rectangle(haystack_img, bottom_left, top_right, 
                        color=(255,255,255), 
                        thickness=2,
                        lineType=cv.LINE_4)
            
            self.click_flag = True
            self.click_x = bottom_left[0] + needle_w / 2
            self.click_y = bottom_left[1] + needle_h / 2
                        
            
        return (self.click_x, self.click_y, haystack_img, self.click_flag, img_type)