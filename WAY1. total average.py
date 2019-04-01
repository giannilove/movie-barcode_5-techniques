#WAY1. total average

import numpy as np
import cv2
import matplotlib.pyplot as plt
import imageio
import random

 

def getColor(frame):
    height, width, depth = frame.shape
    frame_colors = []

    for x in range(int(width)):
        for y in range(int(height)):

            color = frame[y,x]
            frame_colors.append(color)

   # print(frame_colors)
    return frame_colors

 
def avrg(alist):
    red_total = 0 
    green_total = 0
    blue_total = 0

    for x in alist:
        #print(x)
        red = x[0] ; green = x[1] ; blue = x[2]
        #print(red,green,blue)
        red_total += red ; green_total += green ; blue_total += blue
    red = red_total // len(alist)
    green = green_total // len(alist)
    blue = blue_total // len(alist)
    colors = [red, green, blue]

    return colors

 
 

filename='C:\\Users\\user\\Desktop\\[MV]10cm_pet.mp4'
cap = cv2.VideoCapture(filename) 

CList = [] 

while(True): 
    ret, frame = cap.read()

    if ret == False:
        break 

    CList.append(avrg(getColor(frame)))

cap.release()

barcode = np.zeros((1000,len(CList),3)) 


for i in range(len(CList)):
   barcode[:,i] = CList[i]


b, g, r = cv2.split(barcode)   
barcode2 = cv2.merge([r,g,b]) 
barcode2 = barcode2.astype(np.uint8) 

plt.imshow(barcode2)
plt.show()

 
imageio.imwrite('MovieBarcode_WAY1_[MV]10cm_pet.png', barcode2)

cv2.destroyAllWindows()

