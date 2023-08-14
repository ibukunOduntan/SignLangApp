from flask import Flask, render_template, Response
import cv2
from cvzone.ClassificationModule import Classifier
import sign_model
from cvzone.HandTrackingModule import HandDetector

camera_running = False
app = Flask(__name__)
camera = cv2.VideoCapture(0)


@app.route("/")
def home():
  return render_template('home.html')

@app.route("/choose-level")
def choose_level():
  return render_template('levels.html')

@app.route("/text-to-asl")
def text_toASL():
  return render_template('text-to-asl.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/level-one")
def level_one():
     return render_template('level-one.html')

@app.route("/level-two")
def level_two():
     return render_template('level-two.html')

def easy_mode():
    global camera_running
    global camera
    detector = HandDetector(maxHands=1, detectionCon=0.7)
    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    classifier = Classifier("model/TESTWITH643_2.h5", "model/labels.txt")

    while camera_running:
        success, img = camera.read()
        
        if not success:
            break  
    # show the image with the landmarks
    
        try:
            imgOutput, score = sign_model.easy_mode(width, height, img, classifier)
            hands, _ = detector.findHands(imgOutput, draw=True)
        except cv2.error as e:
            continue
        try:
            ret, buffer = cv2.imencode('.png', imgOutput)
            if ret:
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            pass

    # release the camera once the loop is finished
    camera.release()
    camera = None
            
@app.route("/video_feed_l1")
def video_feed_l1():
    return Response(easy_mode(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/start_camera_l1")
def start_camera_l1():
    global camera_running
    global camera
    if not camera_running:
        # camera.release()
        camera = cv2.VideoCapture(0)
        camera_running = True
    return "Camera already running"


@app.route("/stop_camera_l1")
def stop_camera_l1():
    global camera_running
    global camera
    if camera_running:
        camera_running = False
        # camera.release()
        return "Camera stopped"
    return "Camera already stopped"

def hard_mode():
    global camera_running
    global camera
    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    detector = HandDetector(maxHands=1, detectionCon=0.7)

    classifier = Classifier("model/TESTWITH643_2.h5", "model/labels.txt")

    while camera_running:
        success, img = camera.read()
        
        if not success:
            break   
        try:
            imgOutput, score = sign_model.hard_mode(width, height, img, classifier)
            hands, _ = detector.findHands(imgOutput, draw=True)
        except cv2.error as e:
            continue
        try:
            ret, buffer = cv2.imencode('.png', imgOutput)
            if ret:
                    imgOutput = buffer.tobytes()
                    yield (b'--frame\r\n'
                        b'Content-Type: image/png\r\n\r\n' + imgOutput + b'\r\n')
        except Exception as e:
            pass
            
       
        # wait for 0.5 seconds before capturing the next fram

    camera.release()
    camera = None


@app.route('/video_feed_l2')
def video_feed_l2():
    
    return Response(hard_mode(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/start_camera_l2")
def start_camera_l2():
    global camera_running
    global camera
    if not camera_running:
        # camera.release()
        camera = cv2.VideoCapture(0)
        camera_running = True
    return "Camera already running"


@app.route("/stop_camera_l2")
def stop_camera_l2():
    global camera_running
    global camera
    if camera_running:
        camera_running = False
        # camera.release()
        return "Camera stopped"
    return "Camera already stopped"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)