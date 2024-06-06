# webcam

import cv2

cap = cv2.VideoCapture(0)

def show_cap(cap):
    cv2.namedWindow("Capturing", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Capturing", 640, 480)
    while True:

        check, frame = cap.read()
        # print(check, "\n", frame)

        cv2.imshow("Capturing", frame)

        key = cv2.waitKey(1)
        if(key == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows

show_cap(cap)