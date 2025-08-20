from linear_probing_hash_table import LinearProbingHashTable

def two_sum_enhanced(arr, key):
    my_hash = LinearProbingHashTable()

    for i, num in arr:
        # calc the rest to reach this key
        rest = key - num
        # if exist so I found the complement return true
        if my_hash.search(rest) is not None:
            return True
        
        # else insert this new number at new index
        my_hash.insert(num, i)

    return False

print(two_sum_enhanced([1, 2, 3, 4], 6))
print(two_sum_enhanced([5, 1, 7, 3, 9], 8))