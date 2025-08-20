class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self, n):
        # Create circular linked list with n nodes (1 to n)
        if n < 1:
            return
        
        prev = None
        for i in range(1, n + 1):
            new_node = Node(i)
            if not self.head:
                self.head = new_node
                prev = new_node
            else:
                prev.next = new_node
                prev = new_node
        # to make it circular
        prev.next = self.head

    # Time O(n * k) | Space O(1)
    # while n = number of nodes and k is the elimination number
    def eliminate(self, k):

        if not self.head or k < 1:
            return None
        
        if self.head.next == self.head:
            return self.head.data
        
        current = self.head
        prev= None
        # while there are more than one node
        while current != current.next:
            # to loop twice
            for _ in range(k - 1):
                # store the previous one to can remove the current safely
                prev = current
                current = current.next
            # remove the current node
            prev.next = current.next
            # start the next loop
            # start from the next node 
            current = current.next
        
        # when finish and still just one node return it
        return current.data



    def print_list(self):
        if not self.head: 
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data)
            return

        current = self.head.next
        my_string = str(self.head.data) + ' '
        while current != self.head:
            my_string += str(current.data) + ' '
            current = current.next
        print(my_string)

my_list = CircularLinkedList()
my_list.create(5)
my_list.print_list()
print(my_list.eliminate(3))

