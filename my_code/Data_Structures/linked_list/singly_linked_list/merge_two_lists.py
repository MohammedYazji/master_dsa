from singly_linked_list_head import SinglyLinkedList, Node

class Solution:
    # Time: O(n + m)  |  Space: O(1)
    # why ? n + m is the length of the two lists
    # so O(n + m) == O(n)
    @staticmethod
    def merge_two_lists(list1: Node, list2: Node) -> Node:
        # make a new node (list) to store the two lists
        new_node = Node(0)

        # make a pointer to loop over the new list
        current = new_node

        # The loop continues as long as neither list is empty.
        # If one of them becomes None, we exit the loop — because there's nothing more to compare in that list.
        while list1 and list2:
            # If list1 has the smaller value, it should come next in the merged list
            if list1.data < list2.data:
                # Connect the current node to the node from list1, because it’s the smaller one
                current.next = list1
                # Move the pointer in list1 one step
                list1 = list1.next
            else:
                # If list2.val is smaller or equal, do the same logic with list2
                current.next = list2
                list2 = list2.next

            # after each process move the current one step
            current = current.next

        # push the remaining non empty list to my new node list
        if list1:
            current.next = list1
        else:
            current.next = list2

        # return the new node next pointer from where we start build our new list
        return new_node.next

    @staticmethod
    def print_list(head : Node) -> None:
        current = head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# First list: 1 -> 3 -> 5
list1 = SinglyLinkedList()
for node in [1, 3, 5]:
    list1.insert_at_end(node)

# print the first list
print("First list:")
Solution.print_list(list1.head)
########################################
# Second list: 2 -> 4 -> 6
list2 = SinglyLinkedList()
for node in [2, 4, 6]:
    list2.insert_at_end(node)

# print the second list
print("Second list:")
Solution.print_list(list2.head)
########################################
# Merge them
merged_lists = Solution.merge_two_lists(list1.head, list2.head)

# print the merged list
print("Merged list:")
Solution.print_list(merged_lists)

