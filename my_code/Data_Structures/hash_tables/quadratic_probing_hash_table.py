
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class QuadraticProbingHashTable:
    def __init__(self, size=11, threshold=0.7):
        # so if we have size not a prime, find next prime
        # to minimize the collisions
        self.size = self._next_prime(size)
        # the maximum load factor percentage before we resize the hash table
        self.threshold = threshold
        # intialize the table with None values
        self.table = [None] * self.size
        # the count of elements in my table
        self.count = 0
    
    def _hash(self, key):
        """Hash function to convert key to index"""
        if isinstance(key, str):
            # if the key is string: sum ASCII values then mod by size
            total = 0 
            for char in key:
                total += ord(char)
            return total % self.size
        
        elif isinstance(key, int):
            # if the key is integer: just mod by size
            return key % self.size
        else:  
            # if the key is other type: convert to string first, then recall _hash to get the index
            # for example if the key is float, call _hash with str(key)
            return self._hash(str(key)) 
        # ###########
        # or just use the built-in function hash
        # return hash(key) % self.size


    def load_factor(self):
        """Calculate current load factor
        load factor = n / m = elements-count / size
        """
        return self.count / self.size
    
    # Insert and update at same function
    def insert(self, key, value):
        # before insert a new key, if the next insert would exceed the threshold so rehash (resize the table)
        if self.load_factor() >= self.threshold:
            # here we resize the table with the next prime of double the size
            # example if we have size = 6, so new size is the first prime after 12 = 13
            self._rehash(self._next_prime(self.size * 2))
        
        # now by using hash function get the index of this key
        idx = self._hash(key)
        probes = 0
        
        # to ensure that will just loop one loop
        while probes < self.size:
            # check this slot in the table
            # first check the original index when probes is 0
            # then move the index quadratically forward
            probe_idx = (idx + probes * probes) % self.size
            slot = self.table[probe_idx]
            # when i found an empty slot so insert the key there
            if slot is None:
                self.table[probe_idx] = Node(key, value)
                self.count += 1
                return
            
            # if there's key there so update the value
            elif slot.key == key:
                slot.value = value
                return
            # then if there's no empty slot
            # walk forward to the next slot until find an empty slot
            else:
                # increment the number of probes, to check if the table is full, so if the probes is equal to the size then table is full and I loop one loop to reach the original slot
                # but actually it will never happen, because in each insert I check the load factor before insert and rehash if load factor exceeds 0.7
                probes += 1        
    
    def search(self, key):
        # by using hash function get the index of this key
        idx = self._hash(key)

        # again use probes to know if we loop one loop, and track the probe index move
        probes = 0
        
        # if probes equal to size so I loop one loop over all elements
        while probes < self.size:
            # first check the original index when probes is 0 then move the index quadratically forward using probes
            probe_idx = (idx + probes * probes) % self.size
            # get the slot at this index in the table
            slot = self.table[probe_idx]
            # if empty so return None
            if slot is None:
                return None
            # if there's key there so return the value
            elif slot.key == key:
                return slot.value
            # else this key is not in this slot so go forward
            probes += 1
        
        # if we finish the loop without finding the key so return None
        return None
    
    def delete(self, key):
        # by using hash function get the index of this key
        idx = self._hash(key)

        # again use probes to know if we loop one loop over all elements
        probes = 0
        
        # if probes equal to size so I loop one loop over all elements
        while probes < self.size:
            # first check the original index when probes is 0 then move the index quadratically forward using probes
            probe_idx = (idx + probes * probes) % self.size
            # get the slot at this index in the table
            slot = self.table[probe_idx]
            # if empty so return False [no such key to delete]
            if slot is None:
                return False
            # if there's key there so delete it
            if slot.key == key:
                # replace the slot with None
                self.table[probe_idx] = None
                # decrement the count
                self.count -= 1
                return True
            # else this key is not in this slot so go forward
            probes += 1
        
        # if we finish the loop without finding the key so return False
        return False
    
    def _rehash(self, new_size):
        """Resize the hash table when load factor exceeds threshold"""

        # store the old table to mutate it
        old_table = self.table
        # set the size to be the new size
        self.size = new_size
        # make the new table
        self.table = [None] * self.size
        # reset the count before insert the elements all over again
        self.count = 0
        
        # Rehash all existing elements
        for slot in old_table:
            # loop over the old table
            # then if in this slot there's an element
            # insert it into our new table
            if slot is not None:
                self.insert(slot.key, slot.value)
    
    def _is_prime(self, num):
        """Check if a number is prime"""
        if num < 2:
            return False
        i = 2
        # To minimize the time, I loop from 2  to the square root of the number.
        # for example, if I'm checking 16, it's enough to test only to 4 => (2, 3, 4).
        # Because after the square root, the divisors will repeat again.
        # and I need just one case to return False.
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
    
    def _next_prime(self, num):
        """Find the next prime number after the given number"""
        # check if old_size * 2 is prime if not move to the next until find prime one
        while not self._is_prime(num):
            # keep looping until find the next prime
            num += 1
        return num