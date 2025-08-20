class Node:
    # each node in the list has data and pointer to the next one
    def __init__(self, data):
        self.data = data
        self.next = None


# beginning of the list => head
# end of the list => tail
# length tracking in O(1)
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # pushing to the end of the list
    # time complexity => O(1)
    def insert_at_end(self,data):
        #  Receive a data and make a new node
        new_node = Node(data)

        # if there's no head => empty list, length = 0
        # so set the head and tail to be the new Node
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        # else if not empty
        # make the tail point on the new node {the previous tail}
        # then set the tail to be the new node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        # then always increment the length by one
        self.length += 1
        return self
    
    # remove from the end of the list
    # time complexity => O(n) (still needs traversal)
    # to get the node before the last one
    def remove_from_end(self):
        if not self.head: 
            return None
        
        # Single node case
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.length -= 1
            return data

        # start from head
        current = self.head
        # loop until catch the node before the last node
        while current.next and current.next.next:
            current = current.next

        # store the removed node to return it later
        removed_node = current.next
        # set the tail to be the node before it
        self.tail = current
        # update the new tail pointer to refer into None
        self.tail.next = None
        # decrement the length by one
        self.length -= 1

        return removed_node.data
        
    # remove the first element (head) 
    # time complexity => O(1)
    def remove_from_start(self):
        # if empty return None
        if not self.head:
            return None
        
        # else store the current head in a variable to return it
        current_head = self.head
        # set the head to be the current head's next property
        self.head = self.head.next
        # decrement the length
        self.length -= 1

        # check if its empty now so set also the tail to be None
        if self.length == 0:
            self.tail = None

        # return the head after remove it
        return current_head.data

    # add to the beginning (head)
    # time complexity => O(1)
    def insert_at_start(self, data):
        # make a new node
        new_node = Node(data)

        # if it's empty create a node and set the head, tail to be this new node
        if not self.head:
            self.head = new_node
            self.tail = self.head
        
        # just run it if it's not empty so put it in else to not run it always
        else:
            # set this new node next point to the old head
            new_node.next = self.head
            # then set the head to be this new node
            self.head = new_node

        # Always Do THis
        # increment the length
        self.length += 1
        # return the linked list
        return self

    # get node at a specific index
    # time complexity => O(n)
    def get(self, index):
        # first check if the index is valid one
        if index < 0 or index >= self.length:
            return None
        else:
            # loop from zero to the target index
            # then return the node we want
            counter = 0
            current = self.head
            while counter < index:
                current = current.next
                counter += 1
            return current

    # update the data of a node at given index
    # time complexity => O(n)
    def set(self, index, data):
        # use the get method 🩷
        found_node = self.get(index)
        #  change it's data
        if found_node:
            found_node.data = data
            return True
        return False
                
    # insert at specific index 
    # time complexity => O(n)
    def insert(self, index, data):
        # if invalid index return null
        # if equal the length allow => so push a new node
        if index < 0 or index > self.length:
            return False
        
        # if the index equal the length so add new node at end
        # push
        elif index == self.length:
            self.insert_at_end(data)
            return True
        
        #  if the index is zero so add at first
        # unshift
        elif index == 0:
            self.insert_at_start(data)
            return True
        
        # else implement our insert method
        # we will use the get method, but don't need the index itself
        # I want the previous one
        else:
            prev = self.get(index - 1)
            # make a new node
            new_node = Node(data)
            # make it point the next of the previous
            new_node.next = prev.next
            # and set the previous to point on the new node
            prev.next = new_node
            self.length += 1
            return True

    # remove at specific index
    # time complexity => O(n)
    def remove(self, index):

        # if invalid index return false
        if index < 0 or index >= self.length:
            return None
        # if index is the last one pop it
        elif index == self.length - 1:
            return self.remove_from_end()
        # if the first one shift it
        elif index == 0 :
            return self.remove_from_start()
        else:
            # else get the previous node
            prev = self.get(index - 1)
            # and set the prev next
            # to be the next of the next node
            removed = prev.next
            prev.next = prev.next.next
            # prev.next = removed.next
            self.length -= 1
            return removed.data

    def __str__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.val) + ' '
            current = current.next
        return res

