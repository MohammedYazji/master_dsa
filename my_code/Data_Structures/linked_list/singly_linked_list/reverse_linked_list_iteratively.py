from singly_linked_list_head import Node, SinglyLinkedList

class Solution:
    # reverse a linked list [iteratively]
    # time: O(n), memory: O(1)
    def reverseList(self, head: Node) -> Node:
        # previous as null to make the first node point to the None
        # make it the last node
        prev = None
        # set the current (as temp variable) to be the head
        current = head

        while current:
            # in each loop store the next node to not lost the rest of the list
            next_node = current.next
            # then set the current to point to the previous node
            current.next = prev
            # then move the previous node to be the current
            prev = current
            # and move the current to the next node, which we stored it before
            # to process the next one
            current = next_node

        # finally when we exit the loop so current is None, so prev is the old last node [the new head]
        # so set update the head value and return it
        head = prev  
        return head
    

    def printList(self, head: Node) -> None:
        while head:
            print(head.data, end=" -> ")
            head = head.next
        print("None")
    

if __name__ == "__main__":
    l1 = SinglyLinkedList()
    l1.insert_at_end(1)
    l1.insert_at_end(2)
    l1.insert_at_end(3)
    l1.insert_at_end(4)
    l1.insert_at_end(5)
    l1.insert_at_end(6)
    l1.insert_at_end(7)
    l1.insert_at_end(8)
    l1.insert_at_end(9)
    l1.insert_at_end(10)

    s = Solution()
    print("Before reverse:")
    s.printList(l1.head)
    l1.head = s.reverseList(l1.head)
    print("After reverse:")
    s.printList(l1.head)