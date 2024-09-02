import cv2
import numpy as np

def empty(a):
    pass

cap = cv2.VideoCapture(0)
framewidth = 400
frameheight = 250
cap.set(3, framewidth)
cap.set(3, frameheight)
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600, 300)
cv2.createTrackbar("HUE min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("HUE max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("sat min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("sat max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("value min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("value max", "Trackbars", 255, 255, empty)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HUE min", "Trackbars")
    h_max = cv2.getTrackbarPos("HUE max", "Trackbars")
    s_min = cv2.getTrackbarPos("sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("sat max", "Trackbars")
    v_min = cv2.getTrackbarPos("value min", "Trackbars")
    v_max = cv2.getTrackbarPos("value max", "Trackbars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create a mask
    mask = cv2.inRange(imgHSV, lower, upper)

    result=cv2.bitwise_and(img,img,mask=mask)
    mask=cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    stacked=np.hstack([img,mask,result])
    #cv2.imshow("img", img)
    ##cv2.imshow("HSV_img", imgHSV)
    #cv2.imshow("mask", mask)
    #cv2.imshow("result",result)
    cv2.imshow("stacked", stacked)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()