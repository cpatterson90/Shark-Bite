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
        detection_result, rejectLevels, levelWeights= toothCascade.detectMultiScale3(frame,outputRejectLevels=1)
        print(rejectLevels)
        print(levelWeights)
        print(detection_result)
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

def test_image():
    image_path = "test_image.jpg"
    window_name = f"Detected Objects in {image_path}"
    original_image = cv2.imread(image_path)

    # Convert the image to grayscale for easier computation
    image_grey = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)

    cascade_classifier = cv2.CascadeClassifier("cascade//cascade.xml")
    detected_objects = cascade_classifier.detectMultiScale(image_grey)

    # Draw rectangles on the detected objects
    if len(detected_objects) != 0:
        for (x, y, width, height) in detected_objects:
            cv2.rectangle(original_image, (x, y),
                          (x + height, y + width),
                          (0, 255, 0), 2)

    cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(window_name, original_image)
    cv2.resizeWindow(window_name, 400, 400)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #webcam()
    test_image()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
