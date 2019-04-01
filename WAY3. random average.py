#WAY3. random average

import numpy as np
import cv2
import matplotlib.pyplot as plt
import imageio
import random

 

def getColor(frame):
    height, width, depth = frame.shape
    sample_num = height * width // 100 # 1 precent
    frame_colors = []
    for n in range(sample_num):
        y = random.randint(0, int(height)-1)
        x = random.randint(0, int(width)-1)

     #   print(y,x)
        color = frame[y,x]
      #  print(color)
     
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

    return [red, green, blue]

  

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
    #r = CList[i][0]
    #g = CList[i][1]
    #b = CList[i][2]
    barcode[:,i] = CList[i] #:(column) = 전체 = img[0:1000,i] = [r,g,b]

    
b,g,r = cv2.split(barcode) #img파일을 b,g,r로 분리
img2 = cv2.merge([r,g,b]) #b,r을 바꿔서 Merge

img2 = img2.astype(np.uint8) #데이터 타입을 uint8로
plt.imshow(img2)
plt.show()


imageio.imwrite("MovieBarcode_WAY3_[MV]10cm_pet.png",img2)
#이 이름으로 이미지 파일을 만든다

cv2.destroyAllWindows() #cv2.imshow #생성된 모든 윈도우를 제거
