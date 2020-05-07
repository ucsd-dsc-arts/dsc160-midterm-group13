import cv2 as cv
import glob
import os

regex = '([0-9]+)(?=[^\/]*$)'                                                   
                                                                                
files = glob.glob(os.getcwd() + '/data/toy_story_4/*.jpg')  

for fname in files:
    dst = cv.imread(fname)
    print('test!')
    if dst is None:
        continue
    scale_percent = 50# percent of original size
    width = int(dst.shape[1] * scale_percent / 100)
    height = int(dst.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resize = cv.resize(dst, dim)
    cv.imwrite(fname, resize)
