import cv2
#for webcam
import mediapipe as mp
#for hand detection and gestures
import time
#for fps calculation


class handDetector():

    def __init__(self,mode=False,maxHands=2,model_complexity=1,
                 detectionCon=0.5,trackCon=0.5):

        self.mode=mode
        self.maxHands=maxHands
        self.model_complexity=model_complexity
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        #for the webcam to detect hands
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.model_complexity,
                                      self.detectionCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils
        #detects 21 points on the hand and draws to line to visualize it


    def findHands(self,img,draw=True):

        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #convert the image to rbg because it can only track rgb

        self.results=self.hands.process(imgRGB)
        #processing and looking for hands in the webcam
        #print(results.multi_hand_landmarks)
        # #whether hand is detected or not and also gives the coordinates of the hand if detected

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                if draw:

                    self.mpDraw.draw_landmarks(img,handLms,
                                               self.mpHands.HAND_CONNECTIONS)
                    #shows the 21 detection points on the hand  #also draws the points connection

        return img


    def findPosition(self,img,handNo=0,draw=True):

        lm_list=[]

        if self.results.multi_hand_landmarks:

            my_hand=self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(my_hand.landmark):
                # for different hands
                # print(id,lm)
                # #landmark displays x,y,z axis values for the position of hand in decimal places
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # doing for getting location as per pixels
                #print(id, cx, cy)
                lm_list.append([id,cx,cy])

                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0),cv2.FILLED)
                    # draws a circle around the point whose id no is given out the 21 points

        return lm_list



def main():

    #previous time
    pTime=0
    #current time
    cTime=0

    # main loop
    cap = cv2.VideoCapture(0)
    detector=handDetector()


    while True:

        success, img = cap.read()  # capture the video of webcam

        img = detector.findHands(img)
        lm_list=detector.findPosition(img)

        if len(lm_list) != 0:
            print(lm_list)
            #land mark for different points list

        cTime = time.time()
        #current time for fps calculation
        fps = 1 / (cTime - pTime)
        pTime = cTime
        # calculating the frames per second

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC,
                    3, (255, 0, 255),3)
        # display the fps setting its font,thickness,color purple,thickness,position,etc.

        cv2.imshow('image', img)
        # the heading of the webcam video capture

        cv2.waitKey(1)
        # setting the delay


if __name__=='__main__':
    main()