
import cv2
import pyautogui as pag
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import time

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces = 1)

idList =[22,23,24,26,110,157,158,159,160,161,130,243]
start_time = time.time()*1000.0

curr_time = start_time

while True:


    success, img = cap.read()
    img = cv2.flip(img, 1)
    img, faces = detector.findFaceMesh(img , draw = False)

    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 2, (255,0,255), cv2.FILLED)
        
        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]

        #lengthHor, _ = detector.findDistance(leftLeft, leftRight)
        lengthVer, _ = detector.findDistance(leftUp, leftDown)
        cv2.line(img, leftUp, leftDown, (0,200,0), 3)
        blink = int((lengthVer*100))
        #cv2.line(img, leftLeft, leftRight, (0,200,0), 3)

        print(int((lengthVer*100)))

        curr_time = time.time()*1000.0

        if blink <= 1200:
            start_time = curr_time

        if int(curr_time - start_time) >= 10000:
            pag.alert(text="You have'nt blinked from past 10 seconds , to maintain eye health don't continuously stare the screen ", title="Blink Alert")
            start_time = curr_time


    
    cv2.imshow("Image", img)
    cv2.waitKey(1)