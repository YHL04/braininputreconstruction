

import threading
import datetime

from .sound import record_sound
from .eeg import record_eeg
from .visual import record_visual
from .eye_tracker import record_eye


def record_all():
    filename = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
    print("Will save to {}".format(filename))

    timing_re = [-1]
    timing_rs = [-1]
    timing_rv = [-1]
    timing_ri = [-1]
    re = threading.Thread(target=record_eeg, args=(filename, timing_re))
    rs = threading.Thread(target=record_sound, args=(filename, timing_rs))
    # rv = threading.Thread(target=record_visual, args=(filename, timing_rv))
    # ri = threading.Thread(target=record_eye, args=(filename, timing_ri))

    re.start()
    rs.start()
    # rv.start()
    # ri.start()

    re.join()
    print("Finished EEG recording")
    rs.join()
    print("Finished sound recording")
    # rv.join()
    # print("Finished visuals recording")
    # ri.join()
    # print("Finished eyes recording")

    assert abs(timing_re[0] - timing_rs[0]) < .1
    # assert abs(timing_rs[0] - timing_rv[0]) < .1
    # assert abs(timing_rv[0] - timing_ri[0]) < .1


if __name__ == "__main__":
    record_all()

