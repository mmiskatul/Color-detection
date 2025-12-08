import cv2
from util import get_limit



yellow = [0,255,255] # yellow in RGB Colorspace 
cap =cv2.VideoCapture(0)

while True :
    ret ,frame =cap.read()
    frame =cv2.flip(frame,1)
    
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    
    lowerLimit, upperLimit =get_limit(color=yellow)
    mask = cv2.inRange(hsvImage,) 
    
    cv2.imshow("Frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()