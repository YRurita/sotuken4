import cv2

def camera():
    deviceid=0 # it depends on the order of USB connection. 
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    ret, frame = capture.read()
    cv2.imwrite('pics/photo.jpg', frame)
    