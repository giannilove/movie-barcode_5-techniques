# WAY5. center of frame

import numpy as np
import importlib
import matplotlib.pyplot as plt
import cv2
import imageio
import random

# def 함수명(변수):
     # 함수내용
     # return 반환할 값

def getRepColor(img): # getRepColor 함수 생성
    # rc와 cc는 각각 너비, 길이의 중간값
    # img.shape: (height, width, depth), 각각을 인덱싱하면 (0,1,2)
    rc = img.shape[0]//2 # shape[0]은 height
    cc = img.shape[1]//2 # shape[1]은 width
    color = img[rc, cc] # 이미지 안에서 (rc, cc)에 해당하는 좌표
    return color # 함수를 쓰면 img[rc,cc]

filename = 'C:\\Users\\user\\Desktop\\[MV]10cm_pet.mp4' # 동영상 위치
cap = cv2.VideoCapture(filename)

if cap.isOpened() == False:
    print('File open error:', filename) # 오류 있을 시 출력


CList = [] # 빈 리스트 생성

while(True):
    ret, frame = cap.read() # frame은 cap.read()

    if ret == False: #더이상 프레임이 안 남았을 때 while문 종료
        break 

    c = getRepColor(frame) # frame -> img(변수), frame이 c로 반환
    CList.append(c) #CList에 c 추가

cap.release()
img = np.zeros((1000,len(CList),3)) # (세로, 가로, 색깔단위(RGB))

for i in range(len(CList)):
    #r = CList[i][0]
    #g = CList[i][1]
    #b = CList[i][2]
    img[:,i] = CList[i] #:(column) = 전체 = img[0:1000,i] = [r,g,b]

    
b,g,r = cv2.split(img) #img파일을 b,g,r로 분리
img2 = cv2.merge([r,g,b]) #b,r을 바꿔서 Merge

img2 = img2.astype(np.uint8) #데이터 타입을 uint8로
plt.imshow(img2)
plt.show()


imageio.imwrite("MovieBarcode_WAY5_[MV]10cm_pet.png",img2)
#이 이름으로 이미지 파일을 만든다

cv2.destroyAllWindows() #cv2.imshow #생성된 모든 윈도우를 제거
