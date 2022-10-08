from CustomHandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

fingers_to_num = {
    (0,0,0,0,0) : "0",
    (0,1,0,0,0) : "1",
    (0,1,1,0,0) : "2",
    (1,1,1,0,0) : "3",
    (0,1,1,1,1) : "4",
    (1,1,1,1,1) : "5",
    (0,1,1,1,0) : "6",
    (0,1,1,0,1) : "7",
    (0,1,0,1,1) : "8",
    (0,0,1,1,1) : "9"
}

text = ""
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img, text)  # with draw

    if hands:
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        t_fingers1 = tuple(fingers1)
        if t_fingers1 in fingers_to_num:
            text = "Current number " + fingers_to_num[t_fingers1]

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)