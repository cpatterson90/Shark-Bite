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

        # apply classifier?
        teeth = toothCascade.detectMultiScale(frame)
        detection_result, rejectLevels, levelWeights= toothCascade.detectMultiScale3(frame,outputRejectLevels=1)
        print(f"reject Levels: {rejectLevels}")
        print(f"levelweights: {levelWeights}")
        print(f"detection results: {detection_result}")
        # Draw a rectangle around the teeth
        #for (x, y, w, h) in teeth:
        #    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #    cv2.putText(frame, "test", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 255, 0), 2)

        i = 0
        for (x, y, w, h) in detection_result:
            if abs(levelWeights[i]) > .7:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(levelWeights[i]), (x, y), font, 0.5, (255, 255, 255), 1)
            i = i + 1

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

def test_image():
    image_path = "test_image.jpg"
    #image_path = "positive/SharkTooth_1.png"
    window_name = f"Detected Objects in {image_path}"
    original_image = cv2.imread(image_path)

    frame = cv2.resize(original_image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # apply classifier?
    cascade_classifier = cv2.CascadeClassifier("cascade//cascade.xml")
    teeth = cascade_classifier.detectMultiScale(frame)
    detection_result, rejectLevels, levelWeights = cascade_classifier.detectMultiScale3(frame, outputRejectLevels=1)
    print(f"reject Levels: {rejectLevels}")
    print(f"levelweights: {levelWeights}")
    print(f"detection results: {detection_result}")

    # Draw a rectangle around the teeth
    for (x, y, w, h) in teeth:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame,"test", (x,y-10),cv2.FONT_HERSHEY_SIMPLEX, .8,(0,255,0),2)

    #i = 0
    #font = cv2.FONT_ITALIC
    #for (x, y, w, h) in detection_result:
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(frame, str(levelWeights[i][0]), (x, y), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        #i = i + 1

    cv2.imshow('Input', frame)

    cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(window_name, original_image)
    cv2.resizeWindow(window_name, 400, 400)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webcam()
    test_image()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
