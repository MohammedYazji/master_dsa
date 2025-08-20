from linear_probing_hash_table import LinearProbingHashTable

def duplicate_detection(arr):
    my_hash = LinearProbingHashTable()

    duplication_list = []
    for char in arr:
        if my_hash.search(char) is not None:  
            duplication_list.append(char)
        my_hash.insert(char, 0)

    return duplication_list


