import cv2 as cv 
import argparse
import pygame

# Sets basic audio parameters (frequency, size, channels, buffer)
pygame.mixer.init()
song = pygame.mixer.Sound("815667__jadis0x__looping-piano-melody.wav")

channel = pygame.mixer.Channel(0)
# The OpenCv base was provided by chatgpt
cap  = cv.VideoCapture(0)
# argpase act the same as argv agc in C
parser = argparse.ArgumentParser(description = 'This program enable you to make song with your movement ')

parser.add_argument('--algo', type=str, help= 'Background subtraction method (KNN, MOG2)', default = 'MOG2')
args = parser.parse_args()

# choose witch algorithm we gonna use
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()

# Webcam management and observation of frames to "infinite"
if not cap.isOpened():
    print("Impossible d'accéder à la webcam")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
# start of the implementation of Background Subtraction Methods
    fgMask = backSub.apply(frame)

    cv.imshow("FG Mask", fgMask)  
    cv.imshow("Webcam", frame)  


# This logic come from chatgpt, not entirely but especially on the else and unpause part
    if cv.countNonZero(fgMask) > 40000:
        if not channel.get_busy():
            channel.play(song)
        else:
            channel.unpause()
    else:
        channel.pause()

# This part look if the case q is not send every 30 sec to break the while loop 
    if cv.waitKey(30) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()