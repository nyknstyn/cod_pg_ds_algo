from ds.heap.heap import Heap


def sort_array(array:[]):
    heap = Heap()
    heap.build_heap(array)
    index = heap.heap_size
    while index > 1:
        temp = heap.array[index-1]
        heap.array[index-1] = heap.array[0]
        heap.array[0] = temp
        heap.heap_size -= 1
        heap.heapify(1)
        index -= 1
    return heap.array
