import cv2 as cv
import numpy as np


haystack_img = cv.imread('../images/example_main_menu.PNG', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('../images/start_game.PNG', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

cv.imshow('Result', result)
cv.waitKey()