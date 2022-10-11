import numpy as np
import cv2
from mss import mss
from PIL import Image

def webcam():

    cap = cv2.VideoCapture(0)
    cascPath = "cascade//cascade.xml"
    toothCascade = cv2.CascadeClassifier(cascPath)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # apply classifier?
        teeth = toothCascade.detectMultiScale(frame)

        # Draw a rectangle around the teeth
        for (x, y, w, h) in teeth:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def screen():
    bounding_box = {'top': 100, 'left': 2000, 'width': 800, 'height': 600}

    sct = mss()
    cascPath = "cascade//cascade.xml"
    toothCascade = cv2.CascadeClassifier(cascPath)

    while True:
        sct_img = sct.grab(bounding_box)
        gray = cv2.cvtColor(sct_img, cv2.COLOR_BGR2GRAY)

        # apply classifier?
        teeth = toothCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(24, 24),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the teeth
        for (x, y, w, h) in teeth:
            cv2.rectangle(sct_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('screen', np.array(sct_img))

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webcam()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
