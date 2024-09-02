import numpy as np
import cv2

circles=np.zeros((4,2),int)
counter=0

def mousePoints(event,x,y,flags,params) :
    global counter
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[counter]=x,y
        counter=counter+1

path="Resources/cards.jpg"
img=cv2.imread(path)

while True:
    if counter==4:

        height=200
        width=150
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix=cv2.getPerspectiveTransform(pts1,pts2)
        img_output=cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("output image", img_output)

    for x in range(0,counter):
        cv2.circle(img,(int(circles[x][0]),int(circles[x][1])),5,(255,0,0),cv2.FILLED)

    cv2.imshow("original image",img )

    cv2.setMouseCallback("original image",mousePoints)
    if  cv2.waitKey(1) & 0xFF== ord ('q') :
        break