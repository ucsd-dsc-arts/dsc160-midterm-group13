import cv2
import numpy as np
import glob
import os
import re
from os.path import isfile, join

DATA_PATH = './data/toy_story_4/'
OUTPUT_PATH = 'toy_story.avi'
size = (0,0)
frame_data = []
regex = '([0-9]+)(?=[^\/]*$)'

files = glob.glob(os.getcwd() + '/data/toy_story_4/*.jpg')
files = sorted(files, key=lambda x:float(re.findall(regex, x)[0]))
print(files)
for fname in files:
    print('select')
    img = cv2.imread(fname)
    if img is None:
        continue
    height,width, layers = img.shape
    size = (width, height)
    frame_data.append(img)

out = cv2.VideoWriter(OUTPUT_PATH, cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

for i in range(len(frame_data)):
    out.write(frame_data[i])

out.release()
print(len(frame_data))
