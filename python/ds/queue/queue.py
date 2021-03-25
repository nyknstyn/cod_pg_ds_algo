class Queue:

    QUEUE_SIZE = 10

    def __init__(self):
        self.queue = [None for i in range(Queue.QUEUE_SIZE)]
        self.front = 0
        self.rear = 0

    def en_queue(self, data):
        if (self.rear == Queue.QUEUE_SIZE-1 and self.front == 0) or (self.rear == self.front-1):
            raise Exception("Queue size full")
        if self.rear == self.rear == 0 and self.queue[self.rear] is None:
            self.queue[self.rear] = data
            return
        self.rear = (self.rear+1) % Queue.QUEUE_SIZE
        self.queue[self.rear] = data

    def de_queue(self):
        if self.front == self.rear and self.queue[self.rear] is None:
            raise Exception("Queue is Empty")
        data = self.queue[self.front]
        self.queue[self.front] = None
        if self.front != self.rear:
            self.front = (self.front + 1) % Queue.QUEUE_SIZE
        return data

    def print_queue(self):
        print(*self.queue, sep=" ==> ")
