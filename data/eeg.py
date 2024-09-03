

import time
import keyboard


def record_eeg(filename, timing):
    start = time.time()

    while True:
        if keyboard.is_pressed("c"):
            break

    timing[0] = time.time() - start

