from min_heap import MinHeap

class Solution:
    @staticmethod
    def get_k_min_value(k: int, data: list) -> int:
        if k < 1 or k > len(data):
            return

        copy = MinHeap(data)
        
        # k not in the range
        for _ in range(k - 1):
            copy.pop()

        return copy.peek()

my_heap = MinHeap([6, 4, 8, 2, 8, 9, 1, 3, 1, 7])
print(Solution.get_k_min_value(5, my_heap.data))
