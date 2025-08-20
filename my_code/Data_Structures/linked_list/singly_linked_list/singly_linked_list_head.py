class Node:
    # each node in the list has data and pointer to the next one
    def __init__(self, data):
        self.data = data
        self.next = None

# beginning of the list => head
# no tail and no length
class SinglyLinkedList:
    def __init__(self):
        # constructor to initialize a new list
        self.head = None

    # pushing to the end of the list 
    # time complexity => O(n)
    # will start looping from the head until the last node
    def insert_at_end(self, data):
        #  1) Receive a data and make a new node
        new_node = Node(data)

        # 2) if there's no head => empty list
        # so set the head to be the new Node
        if not self.head:
            self.head = new_node
            return self

        # 3) if not empty, loop until the end
        # make a temp variable to not mutate the head and lost the rest of the list
        current = self.head
        # get the last node
        while current.next:
            current = current.next

        # then make the last node point into the new node
        current.next = new_node
        return self
    

    # remove from the end of the list
    # time complexity => O(n)
    # will start looping from the head until the node before the last
    def remove_from_end(self):
        # 1) if the list is empty return None
        if not self.head:
            return None

        # 2) if I have just one node
        # just remove the pointer of the head to be none
        if not self.head.next:
            # save the node before removing
            data = self.head.data
            # set the head to refer into None
            self.head = None
            # then return the data
            return data

        # 3) if I have multiple nodes
        # reach the node before the last node
        current = self.head
        # to get the last node I need to check if there's a next and next next
        while current.next and current.next.next:
            current = current.next

        # so after we finish the loop so we now at the node before the last
        # so store the data of the last node to return it later
        data = current.next.data  
        # and make the node before last point to None => remove last node
        current.next = None 
        # then return the data of the pooped node
        return data
    
    
    # remove the first element (head) 
    # time complexity => O(1)
    def remove_from_start(self):
        # 1) if the list is empty return None
        if not self.head:
            return None

        # 2) store the head to return it later
        data = self.head.data
        # then make the head of the list to be the second node
        self.head = self.head.next
        # then return the data of the old head
        return data

    # add to the beginning (head)
    # time complexity => O(1)
    def insert_at_start(self, val):
        # 1) make the node to insert it
        new_node = Node(val)

        # 2) make the new node to point into the original head
        new_node.next = self.head
        # 3) and set the head to be the new node
        self.head = new_node
        return self
    
    # get node at a specific index
    # time complexity => O(n)
    # we need to reach the node we want by make counter from zero until reach the index
    def get(self, index):
        current = self.head
        # make counter to loop until reach the counter - 1
        counter = 0

        # if there's head so we still in the list so keep going
        while current:
            # if we reach the index we want so return it
            if counter == index:
                return current
            # else keep looping => move the pointer one step => increment the counter
            current = current.next
            counter += 1

        # if we didn't return any value so, index out of bounds
        return None
    
    # update the data of a node at given index
    # time complexity => O(n)
    def set(self, index, data):
        # use the get method 🩷
        found_node = self.get(index)
        #  change it's value, if exist
        if found_node:
            found_node.data = data
            return True
        # if not exist
        return False
    
    # insert at specific index 
    # time complexity => O(n)
    def insert(self, index, val):
        # 1) if the index is zero so add at first
        # insert_at_start
        if index == 0:
            return self.insert_at_start(val)

        # 2) else implement our insert method
        # we will use the get method, but don't need the index itself
        # I want the previous one to add the new node after it
        prev = self.get(index - 1)

        # to ensure that the index is valid
        if not prev:
            return False
        
        # make a new node
        new_node = Node(val)
        # make it point the next of the previous
        new_node.next = prev.next
        # and set the previous to point on the new node
        prev.next = new_node
        return True
    
        # remove at specific index O(n)
    
    # remove at specific index
    # time complexity => O(n)
    def remove(self, index):
        # 1) if the first one 
        # use remove_from_start
        if index == 0:
            return self.remove_from_start()

        # 2) else get the node before this index to set it point to the next next
        # like jump on  the target index
        prev = self.get(index - 1)

        # ensure that the index is valid
        if not prev or not prev.next:
            return None
        
        # and set the prev next
        # to be the next of the next node
        removed = prev.next
        prev.next = removed.next

        return removed.data

    
    # method to return the list length
    def length(self):
        counter = 0
        current = self.head

        while current:
            counter += 1
            current = current.next
        return counter

    def __str__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.data) + ' '
            current = current.next
        return res