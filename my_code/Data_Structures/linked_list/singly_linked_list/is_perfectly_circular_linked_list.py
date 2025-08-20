from circular_singly_linked_list import Node, CircularSinglyLinkedList

class Solution:
    # to check if the linked list tail refer to the head
    # without using tail (harder)
    @staticmethod
    def is_perfectly_circular(head: Node) -> bool:
        """
        Check if linked list is perfectly circular (tail points to head)
        
        Args:
            head: First node of the linked list
            
        Returns:
            bool: True if circular, False otherwise
        """
        if not head:
            return False
        
        # Single node should point to itself to be circular
        if head.next == head:
            return True
        
        current = head.next
        while current and current != head:
            current = current.next

        return current == head


my_list = CircularSinglyLinkedList()
for i in range(1, 6):  
    my_list.insert_at_end(i)

print(my_list)
print("Is perfectly circular:", Solution.is_perfectly_circular(my_list.head))
