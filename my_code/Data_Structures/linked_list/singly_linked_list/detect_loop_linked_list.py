from circular_singly_linked_list import Node, CircularSinglyLinkedList

class Solution:
    @staticmethod
    def floydCycleDetection(head: Node) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if the fast and slow pointers meet so its a loop
            if slow == fast:
                return True
        return False
    

my_list = CircularSinglyLinkedList()
for i in range(1, 6):  
    my_list.insert_at_end(i)


print(my_list)
print("Has loop:", Solution.floydCycleDetection(my_list.head))