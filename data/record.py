

import threading
import datetime

from .sound import record_sound
from .eeg import record_eeg
from .visual import record_visual


def record_all():
    filename = datetime.datetime.now().strftime("%m/%d/%Y,%H:%M:%S")

    re = threading.Thread(record_eeg, filename)
    rs = threading.Thread(record_sound, filename)
    rv = threading.Thread(record_visual, filename)

    re.start()
    rs.start()
    rv.start()

    re.join()
    rs.join()
    rv.join()


if __name__ == "__main__":
    record_all()

