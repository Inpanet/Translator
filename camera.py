import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
#selecting the resolution
for w, h in [(1920,1080), (2560, 1440), (1280,720)]:
    cap.set(3, w); cap.set(4, h)
    if int(cap.get(3)) == w and int(cap.get(4)) == h:
        break

#you can change the frame
cv.namedWindow('frame', cv.WINDOW_NORMAL)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    #flip the frame
    frame = cv.flip(frame, 1)

    cv.imshow('frame', frame)
    #close
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()