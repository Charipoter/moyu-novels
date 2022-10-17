import datetime
from time import sleep


class IntervalTimeCaculator:

    def __init__(self):

        self.start_time = None

        self.end_time = None

        self.interval_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def end(self):
        self.end_time = datetime.datetime.now()
        self.interval_time = (self.end_time - self.start_time).total_seconds()

    def get_interval_time(self):
        return self.interval_time


if __name__ == "__main__":
    time = IntervalTimeCaculator()
    time.start()
    sleep(1.3)
    time.end()
    print(time.get_interval_time())