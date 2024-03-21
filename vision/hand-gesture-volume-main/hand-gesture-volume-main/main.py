import cv2
import mediapipe as mp
import math
import numpy as np
import alsaaudio

# solution APIs
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Volume Control Library Usage
volBar, volPer = 400, 0
minVol, maxVol = alsaaudio.Mixer().getrange()

# Webcam Setup
wCam, hCam = 640, 480
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)

# Mediapipe Hand Landmark Model
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    while cam.isOpened():
        success, image = cam.read()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                print(hand_landmarks)
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

        # multi_hand_landmarks method for Finding postion of Hand landmarks
        lmList = []
        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHand.landmark):
                print(id, lm)
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

        # Assigning variables for Thumb and Index finger position
        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]

            # Marking Thumb and Index finger
            cv2.circle(image, (x1, y1), 15, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.circle(image, (x2, y2), 15, (255, 255, 255), 1, cv2.LINE_AA)

            # Setting Line Color
            line_color = (0, 255, 0)
            length = math.hypot(x2-x1, y2-y1)
            if (length < 20):
                line_color = (0, 0, 255)

            # Setting Line Properties
            line_thickness = 3
            cv2.line(image, (x1, y1), (x2, y2), line_color, 3, cv2.LINE_AA)

            vol = np.interp(length, [20, 130], [minVol, maxVol])
            volBar = np.interp(length, [20, 130], [400, 150])
            volPer = np.interp(length, [20, 130], [0, 100])

            volVirt = float(volPer)
            volVirt /= 100
            volVirt **= 0.4
            volVirt *= 100

            # Volume Bar
            bar_color = (0, 255 * volPer / 100, 255 * (100 - volPer) / 100)
            cv2.rectangle(image, (50, int(volBar)), (85, 400),
                          bar_color, cv2.FILLED, cv2.LINE_AA)
            cv2.rectangle(image, (50, 150), (85, 400),
                          (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_TRIPLEX,
                        1, bar_color, 2, cv2.LINE_AA)

            mixer = alsaaudio.Mixer()
            mixer.setvolume(int(volVirt))

        cv2.imshow('handDetector', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cam.release()
