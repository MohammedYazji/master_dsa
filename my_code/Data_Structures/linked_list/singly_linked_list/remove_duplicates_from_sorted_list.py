from singly_linked_list_head import SinglyLinkedList, Node

class Solution:
    # Time O(n), Space O(1)
    @staticmethod
    def deleteDuplicates(head):
        # make a new pointer
        current = head

        # while the pointer in the list
        while current and current.next:
            # if the current node value equal the next one
            if current.data == current.next.data:
                # make it point into the next next [jump over the similar second node]
                current.next = current.next.next
            # else move one step normally
            current = current.next
        # finally return the head of the list
        return head

    @staticmethod
    def print_list(head : Node) -> None:
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


my_list = SinglyLinkedList()
for n in [1, 1, 2, 3, 3]:
    my_list.insert_at_end(n)

print("Before removing duplicates:")
Solution.print_list(my_list.head)

print('=' * 4)
my_list.head = Solution.deleteDuplicates(my_list.head)

print("After removing duplicates:")
Solution.print_list(my_list.head)
