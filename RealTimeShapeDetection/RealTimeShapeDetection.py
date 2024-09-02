import cv2
import numpy as np
from my_Utils import stackimages

framewidth=400
frameheight=280

cap=cv2.VideoCapture(0)
cap.set(1,framewidth)
cap.set(4,frameheight)


def empty(a):
    pass

cv2.namedWindow("thresholds")
cv2.resizeWindow("thresholds",640,240)
cv2.createTrackbar("threshold1","thresholds",23,255,empty)
cv2.createTrackbar("threshold2","thresholds",20,255,empty)
def get_contours (img,imgcontour):

    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


    for cnt in contours:

        area=cv2.contourArea(cnt)
        if area>1000:
            cv2.drawContours(imgcontour,cnt, -1, (255, 0, 255), 7)
            par1=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02* par1,True)
            print(len(approx))

            x,y,w,h=cv2.boundingRect(approx)
            cv2.rectangle(imgcontour,(x,y),(w+x,y+h),(0,255,0),5)

            cv2.putText(imgcontour, "points: " +str(len(approx)), (x+w+20, y+20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(imgcontour, "Area: " +str(int(area)), (x+w+20, y+45), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)



while True:
    success,image=cap.read()
    imgcontour=image.copy()
    img_blur=cv2.GaussianBlur(image,(5,5),1)
    img_gray=cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)
    threshold1=cv2.getTrackbarPos("threshold1","thresholds")
    threshold2=cv2.getTrackbarPos("threshold2","thresholds")
    img_canny=cv2.Canny(img_gray,threshold1,threshold2)
    kernel=np.ones((5,5))
    img_dilate=cv2.dilate(img_canny,kernel,iterations=1)
    get_contours(img_dilate,imgcontour)
    img_stack=stackimages.stackImages(0.8,([image,img_gray,img_canny],
                                           [img_dilate,img_dilate,imgcontour]))
    cv2.imshow("image",img_stack)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break