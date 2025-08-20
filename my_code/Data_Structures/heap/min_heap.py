class MinHeap:
    def __init__(self, initial_data=None):
        # first create an empty list to store the heap
        self.data = []
        # if we need pass in some initial data so we can build the heap on top of it
        if initial_data:
            self.data = list(initial_data)
            self.build_heap()

    # get the left child of a node using the formula
    def left_child(self, index):
        return 2 * index + 1
    
    # get the right child of a node
    def right_child(self, index):
        return 2 * index + 2
    
    # get the parent of a node
    def parent(self, index):
        return (index - 1) // 2
    
    def heapify_down(self, index):
        # first get the size of the heap to loop just until the last element
        size = len(self.data)
        while True:
            # for current node, get its left and right children
            left = self.left_child(index)
            right = self.right_child(index)

            # suppose the current index as the smallest one
            smallest = index

            # then if the left child is smaller than the current index, then the current index is not the smallest one
            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            # else if the right child is smaller than the current index, then the current index is not the smallest one
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right

            # to exit the loop => if the current index is the smallest one [still and not mutated] break the loop
            if smallest == index:
                break

            # then swap the current index with the smallest one
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            # reset the index to the smallest one to continue looping
            index = smallest

    def heapify_up(self, index):
        while index > 0:
            parent_index = self.parent(index)
            # if the current index is smaller than its parent so we need to swap
            if self.data[index] < self.data[parent_index]:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                # then set the index to the parent of this node to continue looping
                index = parent_index
            else:
                # else the node reach its right position
                break

    def build_heap(self):
        # when we call the constructor, we pass in some initial data so we can build the heap on top of it
        # by use heapify down function while looping to n - 2 / 2
        # why n - 2 / 2: n is the length of the initial data
        for i in range((len(self.data) - 2) // 2, -1, -1):
            self.heapify_down(i)

    def push(self, value):
        # to push a new node push it to the data list
        self.data.append(value)
        # then heapify up to correct the heap start from the new node index up to the root
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            raise IndexError("peek from empty heap")
        # return the root
        return self.data[0]

    # pop from root
    def pop(self):
        if not self.data:
            raise IndexError("pop from empty heap")
        
        elif len(self.data) == 1:
            # if i have just one node so just pop it without heapify
            return self.data.pop()
        
        # else we need to swap the root with the last node
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        # then pop this last node
        # and then heapify down
        min_value = self.data.pop()
        if self.data:
            self.heapify_down(0)
        return min_value
    
    def __len__(self):
        # get the length of the heap
        return len(self.data)

    def __repr__(self):
        # return the string representation of the heap
        return f"MinHeap({self.data})"

    