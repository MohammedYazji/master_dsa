from linear_probing_hash_table import LinearProbingHashTable

def first_non_repeating_char(string):
    my_hash = LinearProbingHashTable()

    # first loop over the string and store each char with its frequency
    for char in string:
        # get the frequency
        freq = my_hash.search(char)  
        # if empty initialize it with 1
        if freq is None:
            my_hash.insert(char, 1)
        else:
            # else add one to it [update it]
            my_hash.insert(char, freq + 1)

    # another loop to find the first char with frequency 1
    # from left to right
    for char in string:
        if my_hash.search(char) == 1:
            return char