import cv2

import mediapipe as mp

import numpy as np

import time

import HandTrackingModule as htm

import math

from ctypes import cast, POINTER

from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities , IAudioEndpointVolume

##################
wCam,hCam=640,480
#heigt and width of webcam window
##################

pTime=0
#variables to calculate fps
cTime=0

 # main loop
cap = cv2.VideoCapture(0)
#to capture the webcam video feed

cap.set(3,wCam)
#setting width and the height
cap.set(4,hCam)

detector=htm.handDetector(detectionCon=0.7)

devices=AudioUtilities.GetSpeakers()

interface=devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL,None
)

volume=cast(interface,POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
vol_range=volume.GetVolumeRange()

min_vol=vol_range[0]
max_vol=vol_range[1]

vol=0
vol_bar=400
vol_percentage=0


while True:

    success, img = cap.read()
    # capture the video of webcam

    img = detector.findHands(img)
    lm_list=detector.findPosition(img,draw=False)

    if len(lm_list) != 0:

        #print(lm_list[4],lm_list[8])

        x1,y1=lm_list[4][1],lm_list[4][2]
        x2, y2 = lm_list[8][1], lm_list[8][2]

        cx,cy=(x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
        # tip of thumb point configuration
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)

        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        # the connection line configuration

        cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
        # the midpoint circle configuration

        length=math.hypot(x2-x1,y2-y1)
        print(int(length))

        #vol range -95 to 0
        #hand range at a particular distance(will change with distance from the camera of the hand) 300 to 0

        vol=np.interp(length,[50,250],[min_vol,max_vol])
        print(vol)

        vol_bar=np.interp(length,[50,250],[400,150])

        vol_percentage = np.interp(length, [50, 250], [0, 100])

        volume.SetMasterVolumeLevel(vol, None)



        if length<50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)

    cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)

    cv2.putText(img, f'{int(vol_percentage)}%', (40, 450), cv2.FONT_ITALIC, 1, (0, 0, 255), 4)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # calculating the frames per second

    cv2.putText(img,f'FPS: {int(fps)}', (10, 30), cv2.FONT_ITALIC, 1, (255, 0, 0),4)
    # display the fps setting its font,thickness,color purple,thickness,position,etc.

    cv2.imshow('image', img)
    # the heading of the webcam video capture
    cv2.waitKey(1)
    # setting the delay