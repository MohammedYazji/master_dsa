from min_heap import MinHeap


class Solution:
    @staticmethod
    def heap_sort(heap: MinHeap) -> list:
        sorted_array = []
        # While the heap is not empty
        while heap.data:           
            # Pop the root (min element) each time
            sorted_array.append(heap.pop())  
        return sorted_array
    

my_heap = MinHeap([6, 4, 8, 2, 8, 9, 1, 3, 1, 7])
print(Solution.heap_sort(my_heap))