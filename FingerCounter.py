import cv2
#for the webcam video capture

import time
#to calculate frames per second

import HandTrackingModule as htm
#the hand tracking module that we have created


#one must download the following packages to run this on their windows computer
#m1 based macbooks would not work because of mediapipe package which in unable to install

#opencv-python
#meiapipe
#hand tracking module in the same folder as this file


wCam,hCam=640,480
#the width and height of the webcam video capture window

cap=cv2.VideoCapture(0)
#initialize webcam video

cap.set(3,wCam)
#3 here is the prop id

cap.set(4,hCam)

pTime=0
#previous time for fps calculation

detector=htm.handDetector(detectionCon=0.7)
#to detect the 21 point on the hand on the webcam video footage

tip_ids=[4,8,12,16,20]
#these are the point id of the tip of each 5 fingers



#main loop
while True:

    success,img=cap.read() #reading the video footage

    img=detector.findHands(img)
    #find hands is a method of the class hand detector in the hand tracking module
    # returns the image

    lm_list=detector.findPosition(img,draw=False)
    #also a method
    # can draw on specefic points or on all points
    #print(lm_list) #shows the position of all the points on the hand per in a list

    if len(lm_list)!=0:    #when hand is detected

        fingers_open=[]

        if lm_list[tip_ids[0]][1] < lm_list[tip_ids[0] - 1][1]:
            #extra for thumb

            fingers_open.append(0)
        else:
            fingers_open.append(1)

        for id in range(1,5):

            # check if the point 8 is below the point 6 of the same finger
            if lm_list[tip_ids[id]][2]<lm_list[tip_ids[id]-2][2]:
                #means finger open  #because of open cv pixels it is reverse
                fingers_open.append(1)
            else:

                fingers_open.append(0)

        print(fingers_open)

        total_fingers_open=fingers_open.count(1)

        cv2.rectangle(img,(20,225),(170,425),
                      (0,0,255),cv2.FILLED)

        cv2.putText(img,str(total_fingers_open), (70, 350),
                    cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)

    cTime=time.time()
    #current time for fps calculation
    fps=1/(cTime-pTime)
    #fps calculation
    pTime=cTime
    #updating the value as the loop executes

                                      #TEXT LOCATION                       #FONT SCALE     FONT THICKNESS
    cv2.putText(img,f'FPS: {int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow("FINGER COUNTER",img)
    # the heading of the window showing the webcam video footage

    cv2.waitKey(1)
    #setting the delay
