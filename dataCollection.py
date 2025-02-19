import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

folder = "Data/test/W"
counter = 0

while True:
    success, img = cap.read()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h/w
        if aspectRatio > 1:
            k = imgSize/h
            wCalc = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop, (wCalc, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCalc)/2)
            imgWhite[:, wGap:wCalc + wGap] = imgResize

        else:
            k = imgSize / w
            hCalc = round(math.ceil(k * h))
            imgResize = cv2.resize(imgCrop, (imgSize, hCalc))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCalc) / 2)
            imgWhite[hGap:hCalc + hGap, :] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    key =cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)


