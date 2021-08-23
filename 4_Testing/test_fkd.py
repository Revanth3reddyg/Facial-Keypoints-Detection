import facialkeypointsdetection
import cv2
#webcam = cv2.VideoCapture(0)
def test_facialkeypoints():
    assert facialkeypointsdetection.FKD.FacialKeypoint(None) != False
