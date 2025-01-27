from collections import deque


class HistoryDict:
    def __init__(self, data=None):
        if data is None:
            data={}
        self.data = data
        self.history = deque(maxlen=5)

    def set_value(self,key,value):
        self.data[key] = value
        self.history.append(key)

    def get_history(self):
        return list(self.history)
