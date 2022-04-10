from contextlib import contextmanager
from datetime import datetime


@contextmanager
def timeit():
    start_time = datetime.now()
    yield None
    end_time = datetime.now()
    print(end_time - start_time)


with timeit():
    [x ** 3 for x in range(9999999)]