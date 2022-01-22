import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import pyautogui as pag
import screen_brightness_control as sbc
from distance_and_window_size import *


cap = cv2.VideoCapture(0)
detector = FaceMeshDetector()
alert = 0

obj = changes()

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]

        left_pupil = face[145]
        right_pupil = face[374]

        w, _info, _image = detector.findDistance(
            left_pupil, right_pupil, img)

        W = 6.3

        f = 600
        D = W*f/w

        cvzone.putTextRect(
            img, f'Distance {int(D)} cm', (face[10][0]-100, face[10][1]-20), 2, 3)

        if D < 30:
            if(alert >= 5):
                pag.alert(text="You are very close to your Display, Doctors recommend to stay atleast 50 cms away from your monitor to avoid eye-strain, We are dimming your monitor's brightness If you are still to close to your monitor", title="Distance Alert")
                alert = 3
                sbc.set_brightness(0)
            else:
                pag.alert(text="You are very close to your Display, Doctors recommend to stay atleast 50 cms away from your monitor to avoid eye-strain", title="Distance Alert")
                alert += 1
        else:
            change(i=int(D), obj=obj)

    '''
    If you want to see Distance of your face from your PC realtime, un-comment the line below
    '''
    # cv2.imshow("Image", img)
    cv2.waitKey(1)
