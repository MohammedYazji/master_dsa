from singly_linked_list_head import  SinglyLinkedList

class Solution:

    # T O(n), S O(1)
    @staticmethod
    def middle_node(head):
        # pointer move one step each time
        step = head
        # pointer move two steps each time
        two_steps = head

        # while the second pointer not none, and has another node after it
        while two_steps and two_steps.next:
            # move one step
            step = step.next
            # move two step
            two_steps = two_steps.next.next
        
        # so when the second pointer reach the end, the first pointer will reach the middle
        # after stop the loop will return the middle node
        return step

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
mid = Solution.middle_node(my_list.head)
print("Middle node value is:", mid.data)

# Using Two Pointers pattern
# Slow, fast pointers
# THIS SOLUTION TAKE Time => O(n), and Space O(1)
# BEST PRACTICE