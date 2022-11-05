import cv2 
import numpy as np
import time

cap = cv2.VideoCapture(0)

#red_range
lower_red = np.array([170,50,50]) #example value
upper_red = np.array([180,255,255]) #example value
#example value
lower_yellow = np.array([22, 93, 0])  #example value
upper_yellow = np.array([45, 255, 255])  #example value

#green_range
lower_green = np.array([52, 0, 55])  #example value
upper_green = np.array([104, 255, 255])  #example value

#blue_range
lower_blue =np.array([150,150,0],np.uint8)  #example value
upper_blue =np.array([180,255,255],np.uint8)  #example value


fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.avi', fourcc, 24.0, (640,480))
print(cap.isOpened)

while True:

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask3 = cv2.inRange(hsv, lower_green, upper_green)
    mask4 = cv2.inRange(hsv, lower_yellow, upper_yellow)
   
    contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours3, hierarchy = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours4, hierarchy = cv2.findContours(mask4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)      

            
    for c in contours1:
        area = cv2.contourArea(c)
        if area > 5000:
            print("Red")
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for c in contours2:
        area = cv2.contourArea(c)
        if area > 5000:
            print("Blue")
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for c in contours3:
        area = cv2.contourArea(c)
        if area > 5000:
            print("Green")
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 

    for c in contours4:
        area = cv2.contourArea(c)
        if area > 5000:
            print("Yellow")
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)                       


    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release() 
cv2.destroyAllWindows()   


      


