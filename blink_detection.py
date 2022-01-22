from turtle import left
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces = 1)

idList =[22,23,24,26,110,157,158,159,160,161,130,243]

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
        #cv2.line(img, leftLeft, leftRight, (0,200,0), 3)

        print(int((lengthVer*100)))
        
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)