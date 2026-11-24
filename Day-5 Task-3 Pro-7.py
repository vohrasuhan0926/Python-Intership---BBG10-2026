import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        total_time = end_time - self.start_time
        print("Time taken:", total_time, "seconds")


# Using Timer context manager
with Timer():
    for i in range(1000000):
        pass