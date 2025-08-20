from singly_linked_list_head import Node, SinglyLinkedList

class Solution:
    # reverse a linked list [recursive]
    # time: O(n), space: O(n) extra space for recursion
    def reverseListRecursive(self, head: Node) -> Node:
        # base case
        # if we reach the last node
        # or if we have just one node return the head
        if head is None or head.next is None:
            return head

        # in the new haed will store the list starting from the last node
        new_head = self.reverseList(head.next)

        # in each recurdion call get the next of the head
        # which is the last node in the new reversed list
        front = head.next
        # make this last node in the new reversed list point into the cuurent node
        front.next = head
        # and make the current node to point into null
        head.next = None
        # finally return the new list
        return new_head
    
    def reverseList(self, head: Node) -> Node:
        return self.reverseListRecursive(head)
    
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