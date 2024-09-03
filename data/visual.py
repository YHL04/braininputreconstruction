

import cv2
import pyautogui
import keyboard
import numpy as np
import time


def record_visual(filename, timing):
    start = time.time()
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    fps = 60.0
    out = cv2.VideoWriter("recordings/visuals/" + filename + ".avi", codec, fps, resolution)

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        out.write(frame)

        if keyboard.is_pressed("c"):
            out.release()
            cv2.destroyAllWindows()
            break

    timing[0] = time.time() - start

