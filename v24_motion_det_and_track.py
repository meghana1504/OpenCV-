

import cv2
import datetime
cap = cv2.VideoCapture(0)

ret1,frame1 = cap.read()
ret2,frame2 = cap.read()

while cap.isOpened():
    key = cv2.waitKey(1)
    #ret,frame = cap.read()
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY) #bcoz contours chaiye easier to find that way
    blur = cv2.GaussianBlur(gray,(5,5),0)
    un,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #DIALATE TO FIND BETTER CONTOURS
    dilated = cv2.dilate(thresh,None,iterations=4)
    #find contours
    conts , un2 = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cont in conts :
        (x,y,wid,hei) = cv2.boundingRect(cont)
        if cv2.contourArea(cont) < 700:
             # continue
            cv2.rectangle(frame1,(x,y),(x+wid,y+hei),(0,255,0),4)
            cv2.putText(frame1,"status:Movement",(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            # dtime = str(datetime.datetime.now())
            # frame1 = cv2.putText(frame1, dtime, (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (2, 4, 5), 2, cv2.LINE_AA)
        # else:
        #     cv2.putText(frame1, "status:Stable", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    #cv2.drawContours(frame1,conts,-1,(0,255,0),3)
    cv2.imshow("The Source",frame1)
    frame1 = frame2
    ret,frame2 = cap.read()
    if key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
