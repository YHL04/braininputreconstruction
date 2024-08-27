
import keyboard
import pyaudio
import wave


def record_sound(filename="output.wave",
                 chunk=1024,
                 sample_format=pyaudio.paInt16,
                 channels=2,
                 fs=44100,
                 ):
    p = pyaudio.PyAudio()

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    while True:
        data = stream.read(chunk)
        frames.append(data)

        if keyboard.is_pressed("c"):
            stream.stop_stream()
            stream.close()
            p.terminate()
            break


    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

