from django.shortcuts import render, redirect
import cv2
import threading
from authentication.opencv.prueba import object

class VideoCaptureThread(threading.Thread):
    def __init__(self, result_object_callback):
        super().__init__()
        self.result_object_callback = result_object_callback
        self.stop_event = threading.Event()

    def run(self):
        cap = cv2.VideoCapture(0)
        while not self.stop_event.is_set():
            ret, frame = cap.read()
            if ret:
                result_object = capture_object(frame)
                self.result_object_callback(result_object)
        cap.release()

    def stop(self):
        self.stop_event.set()
video_capture_thread = None
def start_video_capture(result_emotion_callback):
    global video_capture_thread
    video_capture_thread = VideoCaptureThread(result_emotion_callback)
    video_capture_thread.start()
def stop_video_capture():
    global video_capture_thread
    if video_capture_thread:
        video_capture_thread.stop()
        video_capture_thread.join()
        video_capture_thread = None
def capture_object(imagen):
   
    while True:
        print(object(imagen))
        return object(imagen)
    return 'No es un rostro'


def about(request):
    
    return render(request,"about.html")

def detect_object(request):
    result_object_lock = threading.Lock()
    def result_object_callback(object):
        with result_object_lock:
            print(object)


    start_video_capture(result_object_callback)
    return render(request, 'detect_object/detect_object.html')