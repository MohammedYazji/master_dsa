def two_sum(arr, key):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == key:
                return True
                    
    return False


print(two_sum([1, 2, 3, 4], 6))
print(two_sum([5, 1, 7, 3, 9], 8))