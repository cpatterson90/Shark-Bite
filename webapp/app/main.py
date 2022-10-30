import base64
import os

import cv2
import numpy
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def find_teeth_image(image):
    #image_path = image_location
    #original_image = cv2.imread(image_location)
    object_count = 0

    frame = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    print(frame)
    # apply classifier?
    cascade_classifier = cv2.CascadeClassifier("cascade//cascade.xml")
    teeth = cascade_classifier.detectMultiScale(frame)
    detection_result, rejectLevels, levelWeights = cascade_classifier.detectMultiScale3(frame, outputRejectLevels=1)
    #print(f"reject Levels: {rejectLevels}")
    #print(f"levelweights: {levelWeights}")
    #print(f"detection results: {detection_result}")

    # Draw a rectangle around the teeth
    i = 0
    for (x, y, w, h) in teeth:
        if abs(levelWeights[i]) > .7:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame,f"{round(levelWeights[i],2)}", (x,y-10),cv2.FONT_HERSHEY_SIMPLEX, .8,(0,255,0),2)
            object_count +=1
        i += 1

    return frame, object_count


@app.route("/")
def hello():
    return render_template("home.html")


@app.post("/api/process_image")
def process_image():
    photo = request.files['photo']
    #print(photo)
    if photo:
        if allowed_file(photo.filename):
            # read image file string data
            filestr = request.files['photo']
            file = filestr.read()
            # convert numpy array to image
            frame = cv2.imdecode(numpy.frombuffer(file, numpy.uint8), cv2.IMREAD_COLOR)
            # process the image
            bare_image, objects_detected = find_teeth_image(frame)
            # return base64 encoded image
            b64_image = base64.b64encode(cv2.imencode('.jpg', bare_image)[1]).decode()
            return jsonify({"status": "success", "img": b64_image, "objectsDetected": objects_detected})
        else:
            return jsonify({"status": "error", "reason": "unable to process image: Invalid file type."})

    else:
        return jsonify({"status": "error", "reason": "unable to process image: no image found"})


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
