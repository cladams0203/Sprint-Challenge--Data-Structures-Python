class RingBuffer:
    def __init__(self, capacity):
        self.container = []
        self.capacity = capacity
        self.location = 0

    def append(self, item):
        if len(self.container) < self.capacity:
            self.container.append(item)
            self.location += 1
        elif self.location >= self.capacity:
            self.container[0] = item
            self.location = 1
        else:
            self.container[self.location] = item
            self.location += 1

    def get(self):
        return self.container