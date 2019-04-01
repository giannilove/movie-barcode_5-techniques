import numpy as np

import cv2

import matplotlib.pyplot as plt

import imageio

import random

 

def Colors(frame):

    height, width, depth = frame.shape

    

    colors = np.zeros((256,256,256)) #r,g,b

    for y in range(height):

        for x in range(width):

            p_color = frame[y,x]

            r = p_color[0] ; g = p_color[1] ; b = p_color[2]

            #print(r,g,b)

            colors[r,g,b] +=1

    #print(colors)

    return colors

 

#find the index of the biggest value

def freqColor(alist):

    biggest = 0

    for r in range(256):

        for g in range(256):

            for b in range(256):

                if alist[r,g,b] >= biggest:

                    biggest = alist[r,g,b]

                    final_r = r ; final_g = g ; final_b = b

    freqcolor = [final_r,final_g,final_b]

    return freqcolor

 

filename='C:\\Users\\user\\Desktop\\[Teaser] 10cm_pet.mp4'

cap = cv2.VideoCapture(filename) 

 

CList = []

 

 

while(True): 

    ret, frame = cap.read()

 

    if ret == False:

        break 

 

    CList.append(freqColor(Colors(frame)))

    

 

cap.release()

barcode = np.zeros((1000,len(CList),3)) 

 

 

for i in range(len(CList)):

 

   barcode[:,i] = CList[i]

       

 

b, g, r = cv2.split(barcode)   
barcode2 = cv2.merge([r,g,b]) 

 

barcode2 = barcode2.astype(np.uint8) 

plt.imshow(barcode2)

plt.show()

 

imageio.imwrite('MovieBarcode_WAY4_[Teaser] 10cm_pet.png', barcode2)

 

cv2.destroyAllWindows()
