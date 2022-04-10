from datetime import datetime


class TimerContext:

    def __enter__(self):
        self.start_time = datetime.now()
        return True

    def __exit__(self, ex_type, ex_value, ex_tb):
        self.end_time = datetime.now()

        print(self.end_time - self.start_time)


with TimerContext():
    [x ** 3 for x in range(9999999)]