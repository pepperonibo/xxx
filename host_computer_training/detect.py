import cv2

def detect_thing(img,detector_url):
    detector = cv2.Cascadeclassifier(detector_url)
    detected_things = detector.detect