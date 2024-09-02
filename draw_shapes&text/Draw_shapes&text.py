import cv2
import numpy as np

path="Resources/lena.png"
img=np.zeros((512,512,3),np.uint8)
##img[:]=255,0,0 ##blue image
##cv2.imshow("blue_img",img)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(350,200),(450,100),(0,0,255),cv2.FILLED)
cv2.circle(img,(150,300),50,(255,0,0),cv2.FILLED)
cv2.putText(img,"Draw shapes",(75,50),cv2.FONT_ITALIC,1,(0,115,0),3)
cv2.imshow("img",img)
cv2.waitKey(0)