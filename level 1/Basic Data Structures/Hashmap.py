# https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums):
    val = 0
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1 
        else:
            freq[i]=1

    for i in freq:
        if freq[i] > 1:
            for i in range(1, freq[i]):
                val += i

    return val


# print(numIdenticalPairs([1,2,3,1,1,3]))

def highfrequencychar(s):
    f = {}
    for i in s:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    
    maxi = 0
    val = ""
    for i, j in f.items():
        if j > maxi: 
            maxi = j 
            val = i
    return val

# highfrequencychar("zmszeqxllzvheqwrofgcuntypejcxovtaqbnqyqlmrwitc")

def get_common_element_1(arr1, arr2):
    dicti = {}

    for x in arr1:
        dicti[x]=1
    for x in arr2:
        if x in dicti.keys():
            print(x)
            del dicti[x]
    

# get_common_element_1([1,1,1,2,3,1,1,1,6,6,6,4,4,4,3,3,2,2,1,7,5,6,3,2,1],[1,1,1,3,3,4,4,2,2,2,6,6,6,6])

def get_common_element_2(arr1, arr2):
    hm={}
    for val in arr1:
        if  val in hm:
            hm[val]=hm.get(val)+1
        else:
            hm[val]=1
    for val in arr2:
        if val in hm and hm.get(val)>0:
            print(val)
            hm[val]=hm.get(val)-1


get_common_element_2([1,1,1,2,3,1,1,1,6,6,6,4,4,4,3,3,2,2,1,7,5,6,3,2,1],[1,1,1,3,3,4,4,2,2,2,6,6,6,6])