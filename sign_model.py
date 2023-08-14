import cv2
import numpy as np
import math
from cvzone.HandTrackingModule import HandDetector
from random import random
from english_words import english_words_lower_alpha_set
import time


words = [i for i in sorted(['utensil','love','behave','pride','confident', 'peace', 'garden', 'child']) if ('z' not in i and 'j' not in i) and len(i) > 3 and len(i) <= 10]
start_time = time.time()
curr_time = 0
easy_word_user = ''
easy_word = words[int(random()*len(words))].upper()
easy_word_index = 0

#Main function

offset = 20
imgSize = 300
score = 0

def getLetter(result):
    classLabels ={
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'K',
        10: 'L',
        11: 'M',
        12: 'N',
        13: 'O',
        14: 'P',
        15: 'Q',
        16: 'R',
        17: 'S',
        18: 'T',
        19: 'U',
        20: 'V',
        21: 'W',
        22: 'X',
        23: 'Y',}
    try:
        res = int(result)
        return classLabels[res]
    except:
        return "error"
        


def easy_mode(width, height, img, classifier):
    global easy_word_user, easy_word, easy_word_index, curr_time, score

    detector = HandDetector(maxHands=1)   
    letter_help = cv2.resize(cv2.imread('static/easy_mode_letters/{}.png'.format(easy_word[easy_word_index].lower())), (0,0), fx=0.2, fy=0.2)
    imgOutput = img.copy()
    try:
        cv2.putText(imgOutput, easy_word, (int(width*0.05), int(height*0.95)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_4)
        cv2.putText(imgOutput, easy_word_user, (int(width*0.05), int(height*0.95)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_4)
        cv2.putText(imgOutput, "User score: " + str(score), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    except Exception as e:
        print(e)
    hands, img = detector.findHands(img, draw = True)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        aspectRatio = h / w
        if aspectRatio > 1:
            k = imgSize / h
            wCalc = math.ceil(k * w)
            
            imgResize = cv2.resize(imgCrop, (wCalc, imgSize))
            wGap = math.ceil((imgSize - wCalc) / 2)
    
            imgWhite[:, wGap:wCalc + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw = True)
        else:
            k = imgSize / w
            hCalc = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCalc))
            hGap = math.ceil((imgSize - hCalc) / 2)
            imgWhite[hGap:hCalc + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw = True)
            
        if curr_time < round((time.time() - start_time)/3,1):
                curr_time = round((time.time() - start_time)/3,1)
                try:
                    max_index = np.argmax(prediction)
                    max_value = prediction[max_index]
                    print("Predicted:",getLetter(str(max_index)), ", pred prob:", max_value, ", current index:", easy_word_index, ", current time:", curr_time)
                    if max_value >= 0.8 and getLetter(str(max_index) in ['A','T','S','N','X']):
                        pred_letter = getLetter(str(max_index))
                        if easy_word_index < len(easy_word) and pred_letter == easy_word[easy_word_index] and (easy_word_index == 0 or easy_word[easy_word_index] != easy_word[easy_word_index - 1]):
                            easy_word_user += pred_letter
                            easy_word_index += 1
                            
                        if easy_word_index < len(easy_word) and pred_letter == easy_word[easy_word_index] and easy_word_index > 0 and easy_word[easy_word_index] == easy_word[easy_word_index - 1] :
                            easy_word_user += pred_letter
                            easy_word_index += 1

                    if easy_word_user == easy_word:
                        time.sleep(0.5)
                        score += 1
                        easy_word = words[int(random()*len(words))].upper()
                        easy_word_index = 0
                        easy_word_user = ''

                except Exception as e:
                    print(e)
    imgOutput[5:5+letter_help.shape[0],width-5-letter_help.shape[1]:width-5] = letter_help

    return imgOutput, score
    
        # ret, frame = cap.read()
        
def hard_mode(width, height, img, classifier):
    global easy_word_user, easy_word, easy_word_index, curr_time, score

    detector = HandDetector(maxHands=1)   
    # letter_help = cv2.resize(cv2.imread('static/easy_mode_letters/{}.png'.format(easy_word[easy_word_index].lower())), (0,0), fx=0.2, fy=0.2)
    imgOutput = img.copy()
    try:
        cv2.putText(imgOutput, easy_word, (int(width*0.05), int(height*0.95)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_4)
        cv2.putText(imgOutput, easy_word_user, (int(width*0.05), int(height*0.95)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_4)
        cv2.putText(imgOutput, "User score: " + str(score), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    except Exception as e:
        print(e)
    hands, img = detector.findHands(img, draw = True)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        aspectRatio = h / w
        if aspectRatio > 1:
            k = imgSize / h
            wCalc = math.ceil(k * w)
            
            imgResize = cv2.resize(imgCrop, (wCalc, imgSize))
            wGap = math.ceil((imgSize - wCalc) / 2)
    
            imgWhite[:, wGap:wCalc + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw = True)
        else:
            k = imgSize / w
            hCalc = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCalc))
            hGap = math.ceil((imgSize - hCalc) / 2)
            imgWhite[hGap:hCalc + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw = True)
            
        if curr_time < round((time.time() - start_time)/3,1):
                curr_time = round((time.time() - start_time)/3,1)
                try:
                    max_index = np.argmax(prediction)
                    max_value = prediction[max_index]
                    print("Predicted:",getLetter(str(max_index)), ", pred prob:", max_value, ", current index:", easy_word_index, ", current time:", curr_time)
                    if max_value >= 0.8 and getLetter(str(max_index) in ['A','T','S','N','X']):
                        pred_letter = getLetter(str(max_index))
                        if easy_word_index < len(easy_word) and pred_letter == easy_word[easy_word_index] and (easy_word_index == 0 or easy_word[easy_word_index] != easy_word[easy_word_index - 1]):
                            easy_word_user += pred_letter
                            easy_word_index += 1
                            
                        if easy_word_index < len(easy_word) and pred_letter == easy_word[easy_word_index] and easy_word_index > 0 and easy_word[easy_word_index] == easy_word[easy_word_index - 1] :
                            easy_word_user += pred_letter
                            easy_word_index += 1

                    if easy_word_user == easy_word:
                        time.sleep(0.5)
                        score += 1
                        easy_word = words[int(random()*len(words))].upper()
                        easy_word_index = 0
                        easy_word_user = ''

                except Exception as e:
                    print(e)
    # imgOutput[5:5+letter_help.shape[0],width-5-letter_help.shape[1]:width-5] = letter_help

    return imgOutput, score