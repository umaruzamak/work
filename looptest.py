import nocsmspeech
from functools import wraps
import signal
import os
import time


def handler(signum, frame):
    if signum == signal.SIGINT:
        print('Signal received')


if __name__ == '__main__':
    print('My PID: ', os.getpid())
    signal.signal(signal.SIGINT, handler)

    while True:
        print('Waiting for signal')
        try:
            time.sleep(5)
        except InterruptedError:
            pass


signal.signal(signal.SIGALRM, handler)
# signal.signal(signal.SIGALRM, timeout_handler)
# signal.alarm.timeout(1)


nocsmspeech.Test_Drive.test(1)
nocsmspeech.Test_Drive.listen(1)
