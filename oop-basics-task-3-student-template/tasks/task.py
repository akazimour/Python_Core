class Counter:
    def __init__(self, start=0, stop=None):
        self.start=start
        self.stop = stop
        self.current = start

    def increment(self):
        if self.stop is not None and self.current == self.stop:
            print("The maximal value is reached.")
        else:
            self.current += 1

    def get(self):
        return self.current


