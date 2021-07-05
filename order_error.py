
class OrderError(Exception):
    def __init__(self, food, message):
        self._food = food
        self._message = message

    def message(self):
        return self._message
     
    def food(self):
        return self._food

