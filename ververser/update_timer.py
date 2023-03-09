from time import perf_counter


class UpdateTimer:

    def __init__(self):
        self.start = perf_counter()

    def get_elapsed_time( self ) -> float:
        now = perf_counter()
        return now - self.start

    def restart( self ) -> float:
        elapsed_time = self.get_elapsed_time()
        self.start = perf_counter()
        return elapsed_time
