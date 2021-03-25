# TODO
#   Build Heap
#   Insert Element
#   Extract Min/Max
#   Fetch Min/Max
#   Delete Element
#   Search Element
#   Decrease Value

from heapq import heappush, heappop, heapify
class Heap:
    DEFAULT_MAX_SIZE = 10

    def __init__(self, is_max: bool = True):
        self.is_max = is_max
        self.max_heap_size = Heap.DEFAULT_MAX_SIZE
        self.array = [None for i in range(Heap.DEFAULT_MAX_SIZE)]
        self.heap_size = 0

    def build_heap(self, array: []):
        self.array = array
        self.heap_size = len(array)
        self.max_heap_size = self.heap_size if self.heap_size > self.max_heap_size else self.max_heap_size
        for index in range(int(self.heap_size/2), 0, -1):
            self.heapify(index)

    def print_heap(self):
        print(list(filter(lambda k: k is not None, self.array)))

    def insert(self, data):
        self.__is_heap_full()
        self.array[self.heap_size] = data
        current_index = self.heap_size + 1
        while current_index > 1 and self.array[int(current_index/2)-1] < self.array[current_index-1]:
            temp = self.array[current_index-1]
            self.array[current_index-1] = self.array[int(current_index/2)-1]
            self.array[int(current_index/2)-1] = temp
            current_index = int(current_index/2)
        self.heap_size += 1

    def extract_root(self):
        self.__is_heap_empty()
        data = self.array[0]
        self.array[0] = self.array[self.heap_size-1]
        self.array[self.heap_size-1] = None
        self.heap_size -= 1
        self.heapify(1)
        return data

    def peek_root(self):
        self.__is_heap_empty()
        return self.array[0]

    def heapify(self, index):
        left = 2 * index
        right = (2 * index) + 1
        if left > self.heap_size:
            return
        if self.array[left-1] > self.array[index-1]:
            largest = left
        else:
            largest = index
        if right <= self.heap_size and  self.array[right-1] > self.array[largest-1]:
            largest = right
        if largest != index:
            temp = self.array[index-1]
            self.array[index-1] = self.array[largest-1]
            self.array[largest-1] = temp
            self.heapify(largest)

    def increase_heap_size(self):
        pass

    def __is_heap_full(self):
        if self.heap_size == self.max_heap_size:
            raise Exception("Heap is Full")

    def __is_heap_empty(self):
        if self.heap_size == 0:
            raise Exception("Heap Is Empty")

