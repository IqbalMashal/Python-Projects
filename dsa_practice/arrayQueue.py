class Queue:
    def __init__(self, size):
        self.data_ = [None] * size  # Initialize with None or a specific value
        self.front_ = 0
        self.back_ = 0
        self.numInQueue_ = 0

    def enqueue(self, data):
        if self.numInQueue_ != len(self.data_):
            self.data_[self.back_] = data
            self.back_ = (self.back_ + 1) % len(self.data_)
            self.numInQueue_ += 1
        else:
            raise Exception("Queue is full")

    def dequeue(self):
        if self.numInQueue_ > 0:
            data = self.data_[self.front_]
            self.front_ = (self.front_ + 1) % len(self.data_)
            self.numInQueue_ -= 1
            return data
        else:
            raise Exception("Queue is empty")

    def isEmpty(self):
        return self.numInQueue_ == 0
    
    def isFull(self):
        return self.numInQueue_ == len(self.data_)
    
    def front(self):
        if self.numInQueue_ > 0:
            return self.data_[self.front_]
        else:
            return None  # or raise an exception
        


d1 = Queue(10)

d1.enqueue(1)
d1.enqueue(2)
d1.enqueue(3)
d1.enqueue(4)
d1.enqueue(5)

print(d1.dequeue())

