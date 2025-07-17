import cv2 as cv 
import argparse
# The OpenCv base was provided by chatgpt
cap  = cv.VideoCapture(0)
# argpase act the same as argv agc in C
parser = argparse.ArgumentParser(description = 'This program enable you to make song with your movement ')

parser.add_argument('--algo', type=str, help= 'Background subtraction method (KNN, MOG2)', default = 'MOG2')
args = parser.parse_args()

if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()

if not cap.isOpened():
    print("Impossible d'accéder à la webcam")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break

    fgMask = backSub.apply(frame)

    cv.imshow("FG Mask", fgMask)  
    cv.imshow("Webcam", frame)  

    if cv.countNonZero(fgMask) > 30000:
        print("wazaaaa")
    if cv.waitKey(30) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()