from singly_linked_list_head import SinglyLinkedList

class Solution:
    # T O(n), Space O(1)
    @staticmethod
    def middle_node_by_length(head):
        # make new pointer to not mutate the original head
        current = head

        length = 0
        counter = 0

        # First: calculate length
        while current:
            current = current.next
            length += 1

        # Second: go to the middle
        # Reset the pointer to loop again
        current = head
        while counter < length // 2:
            current = current.next
            counter += 1

        return current

    @staticmethod
    def display(head):
        # print the linked list
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")


my_list = SinglyLinkedList()
for i in range(1, 6):  
    my_list.insert_at_end(i)

Solution.display(my_list.head)
mid = Solution.middle_node_by_length(my_list.head)
print("Middle node value is:", mid.data)


# Calc the length first, then loop until the mid  => length // 2
# THIS SOLUTION TAKE Time => O(n), and Space O(1)
# same as the first solution 
# but in interviews prefer the first one