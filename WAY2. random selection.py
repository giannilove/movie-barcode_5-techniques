import numpy as np
import cv2
import matplotlib.pyplot as plt
import imageio
import random

def getRandomColor(img):
    height, width, depth = img.shape
    rrandom = random.randint(0, int(height)-1)
    crandom = random.randint(0, int(width)-1)
    color = img[rrandom,crandom]
    return color

filename='C:\\Users\\user\\Desktop\\[MV]10cm_pet.mp4'
cap = cv2.VideoCapture(filename) 

 
CList = []

 
while(True): 
    ret, frame = cap.read()
    if ret == False:
        break
    c = getRandomColor(frame)
    CList.append(c)

cap.release()
img = np.zeros((1000,len(CList),3))  
 

for i in range(len(CList)):
    img[:,i] = CList[i] 

 

b, g, r = cv2.split(img)  
img2 = cv2.merge([r,g,b]) 
img2 = img2.astype(np.uint8) 

 
plt.imshow(img2)
plt.show() 

imageio.imwrite('MovieBarcode_WAY2_[MV]10cm_pet.png', img2)

cv2.destroyAllWindows()
