import cv2
import numpy as np

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError('Could not start camera.')

try:
    while True:
        success, frame = camera.read()

        if not success:
            break

        green = np.uint8([[[0, 0, 255]]])
        hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
        print(hsv_green)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red_00 = np.array([0, 100, 100])
        upper_red_00 = np.array([10, 255, 255])

        lower_red_01 = np.array([0, 100, 100])
        upper_red_01 = np.array([10, 255, 255])

        lower_green = np.array([35, 100, 100])
        upper_green = np.array([85, 255, 255])

        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        redLowMask = cv2.inRange(hsv, lower_red_00, upper_red_00)
        redUpMask = cv2.inRange(hsv, lower_red_01, upper_red_01)
        greenMask = cv2.inRange(hsv, lower_green, upper_green)
        blueMask = cv2.inRange(hsv, lower_blue, upper_blue)

        res = cv2.bitwise_or(redLowMask, greenMask, blueMask)

        cv2.imshow('frame', frame)
        cv2.imshow('res', res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
