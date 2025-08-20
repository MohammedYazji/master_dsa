from circular_singly_linked_list import CircularSinglyLinkedList

class Solution:
    # T O()
    @staticmethod
    def reverse(cll: CircularSinglyLinkedList) -> CircularSinglyLinkedList:
        # if reach the last node stop
        if not cll.head or cll.head.next == cll.head:
            return cll
        
        # Start from tail to make circular link work
        prev = cll.tail  
        current = cll.head

        while True:
            # in each loop store the next node to not lost the rest of the list
            next_node = current.next
            # then set the current to point to the previous node
            current.next = prev
            # then move the previous node to be the current
            prev = current
            # and move the current to the next node, which we stored it before
            # to process the next one
            current = next_node

            # Once we loop back to the original head, we’re done
            if current == cll.head:
                break

        # swap head and tail
        cll.head, cll.tail = cll.tail, cll.head

        return cll
    

my_list = CircularSinglyLinkedList()
for i in range(1, 6):  
    my_list.insert_at_end(i)

print(my_list)
print("Reversed:")
print(Solution.reverse(my_list))