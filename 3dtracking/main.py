import cv2 as cv
import socket
from cvzone.HandTrackingModule import HandDetector

width,height = 1280,720
capture = cv.VideoCapture(0)
capture.set(3,width)
capture.set(4,height)

detector = HandDetector(maxHands=1,detectionCon=0.8)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)
while True:
    
    success, img = capture.read()
    hands,img = detector.findHands(img)
    data = []
    if hands:
        hand = hands[0]
        lmList = hand['lmList']
        print(lmList)
        for lm in lmList:
            data.extend([lm[0],height - lm[1],lm[2]])
            print(data)
            sock.sendto(str.encode(str(data)),serverAddressPort)
    img = cv.resize(img,(0,0),None,0.5,0.5)        
    cv.imshow("video",img)
    cv.waitKey(1)
    