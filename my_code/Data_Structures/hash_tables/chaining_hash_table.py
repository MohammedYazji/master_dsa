class Node:
    def __init__(self, key, value):
        # here in chaining we use linked list
        # so each node will have key, value and next
        self.key = key
        self.value = value
        self.next = None

class ChainingHashTable:
    def __init__(self, size):
        # initialize the table with specified size
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        # first we get the index of this key in the table
        index = self._hash(key)
        
        # then we get the node at this index
        # get the linked list inside this bucket
        node = self.table[index]
        
        # if empty list the node will be None
        if node is None:
            # so make a new node and insert it in this index
            self.table[index] = Node(key, value)
        else:
            # else if we have a list so loop over it
            while node.next:
                # if we find the key so update the value and stop
                if node.key == key:
                    node.value = value
                    return
                # else go forward
                node = node.next
            # if we finish the loop without finding the key
            # so we reach to the end of the list
            # so again in the last node if we find the key so update the value
            if node.key == key:
                node.value = value
            # else make a new node and insert it in the end
            else:
                node.next = Node(key, value)
    
    def delete(self, key):
        # first we get the index of this key
        index = self._hash(key)
        # then we get the node at this index
        node = self.table[index]

        # prev pointer to store the previous node and make it jump over the current node [to delete the current node]
        prev = None
        
        # start from the first node
        while node:
            # if we find the key we have two options
            if node.key == key:
                # 1. if it's not the first node just make the previous node jump over the current node
                if prev:
                    prev.next = node.next
                # 2. else if it's the first node so prev still none so just update this bucket and set the first node to be the second one
                else:
                    self.table[index] = node.next
                # then return True
                return True
            # in each iteration we moce the previous node to be the current one
            # and the current node to be the next one
            prev, node = node, node.next
        # if we finish the loop without finding the key
        return False
    
    def search(self, key):
        # first get the index of this key
        index = self._hash(key)
        # and get the list inside this index
        node = self.table[index]
        
        # start from the first node
        while node:
            # if we find the key
            if node.key == key:
                return node.value
            # else go forward
            node = node.next
        # if we finish the loop without finding the key, so return None
        return None
