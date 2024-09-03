import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import keyboard


def record_eye(filename, timing):
    start = time.time()
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()

    coors = []

    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                coors.append([x, y])
                # draw circle on screen
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            # clicks there screen when blinked
            # if (left[0].y - left[1].y) < 0.004:
            #     pyautogui.click()
            #     pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)
        if keyboard.is_pressed("c"):
            coors = np.array(coors)
            np.save("recordings/eyes/" + filename + ".npy", coors)
            break

    timing[0] = time.time() - start


if __name__ == "__main__":
    record_eye("testing")

