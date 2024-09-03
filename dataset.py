

import torch

from scipy.io import wavfile
import os


def read_audio_files():
    files = os.listdir("recordings/sounds/").sort()
    datas = []
    for file in files:
        samplerate, data = wavfile.read("recordings/sounds/" + file)
        datas.append(data)
    return datas


def read_eeg_files():
    files = os.listdir("recordings/sounds/").sort()
    datas = []
    for file in files:
        pass


def read_visual_files():
    files = os.listdir("recordings/sounds/").sort()
    datas = []
    for file in files:
        pass


def read_eye_files():
    files = os.listdir("recordings/sounds/").sort()
    datas = []
    for file in files:
        pass


class AudioOnly(torch.utils.data.Dataset):

    def __init__(self, B, W, H, C, S):
        self.B = B
        self.W = W
        self.H = H
        self.C = C
        self.S = S

    def __getitem__(self):
        inputs = torch.zeros(self.B, self.H, self.W, self.C)
        targets = torch.zeros(self.B, self.S)

        return inputs, targets


class AudioVisual(torch.utils.data.Dataset):

    def __init__(self, B, W, H, C, S):
        self.B = B
        self.W = W
        self.H = H
        self.C = C
        self.S = S

    def __getitem__(self):
        inputs = torch.zeros(self.B, self.H, self.W, self.C)
        visuals = torch.zeros(self.B, self.H, self.W, self.C)
        audios = torch.zeros(self.B, self.S)

        return inputs, visuals, audios


if __name__ == "__main__":
    datas = read_audio_files()
    print(datas[0])
