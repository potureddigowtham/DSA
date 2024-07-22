def two_sum(data, k):
    ''' Two pointer appraoch'''
    l, r = 0, len(data)-1

    while l < r:
        _sum = data[l] + data[r]
        if _sum == k:
            return [l, r]
        elif _sum < k:
            l += 1
        else:
            r -= 1

    return []

print(two_sum([1, 2, 3, 4, 6], 6))
print(two_sum([2, 5, 9, 11], 11))

def remove_duplicates(data):
    ''' Two pointer approach'''
    l, r, n = 0, 0, len(data)-1
    while l < n and r <= n:
        pass
        



print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
