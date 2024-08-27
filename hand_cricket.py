import cv2
import time
import os


wCam,hCam = 640,480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4,hCam)

folderpath = "finger"
myList = os.listdir(folderpath)

overlayList = []
for i in myList:
    image = cv2.imread(f'{folderpath}/{i}')
    overlayList.append(image)
# print(len(overlayList))
pTime = 0
while True:
    success,img = cap.read()

    h,w,c = overlayList[5].shape
    img[0:h,0:w] = overlayList[5]

    cTime = time.time()
    fps = 1/ (cTime-pTime)
    pTime = cTime
    cv2.putText(img,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)