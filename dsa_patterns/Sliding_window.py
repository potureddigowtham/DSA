def continous_average(data, window_size):
    ''' Brute force solution '''
    res = []
    for i in range(len(data) - window_size+1):
        avg = sum(data[i:i+window_size]) / window_size
        res.append(avg)  
    
    return res

def sliding_continous_average(data, window_size):
    ''' Sliding window solution '''
    res = []
    _sum, start = 0, 0
    for end, val in enumerate(data):
        _sum += val

        if end >= window_size - 1:
            res.append(_sum / window_size)
            _sum -= data[start]
            start += 1        
            
    return res

# print(continous_average([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
# print(sliding_continous_average([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))

def maximun_sum_subarray(data, window_size):
    ''' Sliding window solution '''
    res = 0
    _sum, start = 0, 0

    for end, val in enumerate(data):
        _sum += val

        if end >= window_size - 1:
            res = max(res, _sum)
            _sum -= data[start]
            start += 1

    return res

# print(maximun_sum_subarray([2,1,5,1,3,2], 3))
# print(maximun_sum_subarray([2,3,4,1,5], 2))

def find_min_sub_array(data, s):
    ''' Sliding window solution '''
    res, _sum, start = float('inf'), 0, 0

    for end, val in enumerate(data):
        _sum += val

        while _sum >= s:
            res = min(res, (end - start)+1)
            _sum -= data[start]
            start += 1

    if res == float('inf'):
        return 0
    return res

# print(find_min_sub_array([2, 1, 5, 2, 3, 2], 7))
# print(find_min_sub_array([2, 1, 5, 2, 8], 7))
# print(find_min_sub_array([3, 4, 1, 1, 6], 8))

        
def find_long_substr_with_k_distinct(data, k):
    ''' Sliding window solution '''
    res, hashmap, start = 0, {}, 0

    for end, val in enumerate(data):
        if val not in hashmap:
            hashmap[val] = 0
        hashmap[val] += 1

        substr_len = len(hashmap)
        while substr_len > k:
            if hashmap[data[start]] == 1:
                del hashmap[data[start]]
            else:
                hashmap[data[start]] -= 1
            start += 1
            substr_len = len(hashmap)
        
        res = max(res, sum(hashmap.values()))

    return res


# print(find_long_substr_with_k_distinct("araaci", 2))
# print(find_long_substr_with_k_distinct("araaci", 1))
# print(find_long_substr_with_k_distinct("cbbebi", 3))


def fruit_and_basket(fruits):
    ''' Sliding window solution '''
    res, start, basket = 0, 0, {}
    for end, val in enumerate(fruits):
        if val not in basket:
            basket[val] = 0
        basket[val] += 1

        if len(basket) > 2:
            print(basket,"in")
            if basket[fruits[start]] > 1:
                basket[fruits[start]] -= 1
            else:
                del basket[fruits[start]]
            start += 1

        res = max(res, sum(basket.values()))
        print(basket)
    return res

# print(fruit_and_basket(['A', 'B', 'C', 'A', 'C']))
# print(fruit_and_basket(['A', 'B', 'C', 'B', 'B', 'C']))

def non_repeating_substring(s):
    ''' Sliding window solution '''
    res, start, _map = 0, 0, {}
    for end, val in enumerate(s):
        if val in _map:
            start = max(start, _map[val]+1)
        _map[val] = end
        res = max(res, end-start+1)

    return res

# print(non_repeating_substring("aabccbb"))
# print(non_repeating_substring("abbbb"))
# print(non_repeating_substring("abccde"))


def length_of_longest_substring_with_k_distinct_characters(s, k):
    ''' Sliding window solution '''
    res, start, _map, max_rep_count = 0, 0, {}, 0
    for end, val in enumerate(s):
        if val not in _map:
            _map[val] = 0
        _map[val] += 1
        max_rep_count = max(max_rep_count, _map[val])
        if (end - start+1 - max_rep_count) > k:
            _map[s[start]] -= 1
            start += 1
        res = max(res, end - start + 1)
    return res

# print(length_of_longest_substring_with_k_distinct_characters("aabccbb", 2))
# print(length_of_longest_substring_with_k_distinct_characters("abbcb", 1))
# print(length_of_longest_substring_with_k_distinct_characters("abccde", 1))

def longest_substring_with_k_0_replace(data, k):
    ''' sliding windows solution'''
    res, start, max_1_count = 0, 0, 0
    for end, val in enumerate(data):
        if val == 1:
            max_1_count += 1

        if end - start + 1 - max_1_count > k:
            if data[start] == 1:
                max_1_count -= 1
            start += 1
        
        res = max(res, end - start +1)
    return res

# print(longest_substring_with_k_0_replace([0,1,1,0,0,0,1,1,0,1,1], 2))
# print(longest_substring_with_k_0_replace([0,1,0,0,1,1,0,1,1,0,0,1,1], 3))