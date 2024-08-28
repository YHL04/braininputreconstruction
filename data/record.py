

import threading

from .sound import record_sound
from .eeg import record_eeg
from .visual import record_visual


def record_all():
    re = threading.Thread(record_eeg)
    rs = threading.Thread(record_sound)
    rv = threading.Thread(record_visual)

    re.start()
    rs.start()
    rv.start()

    re.join()
    rs.join()
    rv.join()


if __name__ == "__main__":
    record_all()

