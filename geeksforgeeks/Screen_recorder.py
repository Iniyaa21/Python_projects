import numpy
import pyautogui
import cv2

filename = "screen_vid.avi"
resolution = 1920, 1080
fps = 60.0
codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(filename, codec, fps, resolution)

# create and resize window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while 1:
    img = pyautogui.screenshot()
    frame = numpy.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Live", frame)

    if cv2.waitKey(1) == ord('q'):
        break
