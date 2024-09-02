import cv2

path="HaarCascade/cascade.xml"

objectName="Arduino"
framewidth=640
frameheight=480

color=(0,255,0)


cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)


def empty(a):
    pass


cv2.namedWindow("Result")
cv2.resizeWindow("Result",640,240)
cv2.createTrackbar("scale","Result",400,1000,empty)
cv2.createTrackbar("Neig","Result",8,20,empty)
cv2.createTrackbar("MIn_area","Result",0,10000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)


##load our cascade
cascade=cv2.CascadeClassifier(path)

while True:
    success,image=cap.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    scaleVal=1+(cv2.getTrackbarPos("scale","Result")/1000)
    neig=cv2.getTrackbarPos("Neig","Result")
    Brightness=cv2.getTrackbarPos("Brightness","Result")
    cap.set(10,Brightness)

    objects=cascade.detectMultiScale(gray,scaleVal,neig)     ##to perform the detection

    for (x,y,w,h) in objects:
        area=w*h
        minarea=cv2.getTrackbarPos("MIn_area","Result")
        if area>minarea:
            cv2.rectangle(image, (x, y), (w + x, y + h), color, 3)

            cv2.putText(image,objectName, (x ,y-5), cv2.FONT_HERSHEY_COMPLEX, 1,color , 2)
            

    cv2.imshow("Result",image)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
