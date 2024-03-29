class Solution:
    def bubble(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection(self,arr):
        for i in range(len(arr)):
            min = i
            for j in range(i+1,len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[min], arr[i] = arr[i], arr[min]
        return arr

    def insertion(self,arr):
        for i in range(1, len(arr)):
            value = arr[i]
            hole = i
            while (hole > 0 and arr[hole - 1] > value):
                arr[hole] = arr[hole - 1]
                hole -= 1
            arr[hole] = value
        return arr 

    def merge2arrays(self, arr1, arr2):
        arr3 = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr3.append(arr1[i])
                i += 1
            else:
                arr3.append(arr2[j])
                j += 1

        while i < len(arr1):
            arr3.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            arr3.append(arr2[j])
            j += 1

        return arr3

    def mergesort(self, arr):
        if len(arr) < 2:
            return arr
        n = int(len(arr)/2)
        l = self.mergesort(arr[:n])
        r = self.mergesort(arr[n:])
        return self.merge2arrays(l,r)

    def pivot(self, arr, lo, hi):
        p = arr[hi]
        i = lo
        j = lo
        while i <= hi:
            if arr[i] > p:
                i += 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
        return j-1

    def quicksort(self, arr, lo, hi):
        if len(arr) <= 1:
            return arr
        if lo < hi:
            pi = self.pivot(arr, lo, hi)
            self.quicksort(arr, lo, pi-1)
            self.quicksort(arr, pi+1, hi)
        return arr

    def quickselect(self, arr, k, lo, hi):
        pi = self.pivot(arr, lo, hi)
        if k > pi:
            return self.quickselect(arr, k, pi+1, hi)
        elif k < pi:
            return self.quickselect(arr, k, lo, pi-1)
        else:
            return arr[pi]

    def countsort(self, arr, min, max):
        fre = [0]* (max - min + 1)
        for i in arr:
            fre[i-min] += 1
        for j in range(1, len(fre)):
            fre[j] = fre[j] + fre[j-1]
        print(arr)
        print(fre)
        ans = [0]*len(arr)
        for k in range(len(arr)-1, -1, -1):
            val = arr[k]
            pos = fre[val - min] - 1
            ans[pos] = val
            fre[val - min] -= 1
        return ans

    def radixsort(self, arr):
        maxi = max(arr)
        exp = 1
        while exp <= maxi:
            self.countsort_for_radix(arr, int(exp))
            exp *= 10
        return arr

    def countsort_for_radix(self, arr, exp):
        fre = [0]*10
        for i in arr:
            fre[int((i / exp) % 10)] += 1
        for j in range(1, len(fre)):
            fre[j] = fre[j] + fre[j-1]
        print(arr)
        print(fre)
        ans = [0]*len(arr)
        for k in range(len(arr)-1, -1, -1):
            pos = fre[int((arr[k] / exp) % 10)] - 1
            ans[pos] = arr[k]
            fre[int((arr[k] / exp) % 10)] -= 1
        for h in range(len(arr)):
            arr[h] = ans[h]

    def sortdates(self, arr):
        self.countsort_for_sortdates(arr, 1000000, 100, 32)
        self.countsort_for_sortdates(arr, 10000, 100, 13)
        self.countsort_for_sortdates(arr, 1, 10000, 2501)
        return arr

    def countsort_for_sortdates(self, arr, exp1, exp2, rangee):
        fre = [0]*rangee
        for i in arr:
            fre[int((i / exp1) % exp2)] += 1
        for j in range(1, len(fre)):
            fre[j] = fre[j] + fre[j-1]
        ans = [0]*len(arr)
        for k in range(len(arr)-1, -1, -1):
            pos = fre[int((arr[k] / exp1) % exp2)] - 1
            ans[pos] = arr[k]
            fre[int((arr[k] / exp1) % exp2)] -= 1
        for h in range(len(arr)):
            arr[h] = ans[h]

    def sort01(self, arr):
        pivot = 0
        i = 0
        j = 0
        while i < len(arr):
            if arr[i] > pivot:
                i += 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
        return arr

    def sort012(self, arr):
        i = 0
        j = 0
        k = 0
        while i < len(arr):
            if arr[i] == 0:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
                if arr[i] != 1:
                    i += 1
            elif arr[i] == 1:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
                if arr[i] != 0:
                    i += 1
            else:
                i += 1
        return arr

    def target_sum_pair(self, arr, target):
        arr = sorted(arr)
        i = 0
        j = len(arr)-1
        while i < j:
            if arr[i]+arr[j] > target:
                j -= 1
            elif arr[i]+arr[j] < target:
                i += 1
            else:
                print(arr[i], arr[j])
                i += 1
                j -= 1

    def pivot_in_sorted_rotated_array(self, arr) -> int:
        i = 0
        j = len(arr)-1
        while i != j:
            mid = int((i+j)/2)
            if arr[mid] < arr[j]:
                j = mid
            elif arr[mid] >= arr[i]:
                i = mid+1
        return arr[i]

ll = Solution()
# print(ll.quicksort([1,39,5,56,2,14,7,18,9,10], 0, 9))
# print(ll.quickselect([7, 10, 4, 3, 20, 15], 3, 0, 5))
# print(ll.radixsort([956, 61, 31223, 51, 32, 4, 3212, 90, 6112, 34, 56, 21154, 28, 19, 49]))
# print(ll.sortdates([12041996, 20101996, 5061997, 12041989, 11081987]))
# print(ll.sort01([0,1,1,1,0,0,1,0,1,0,1,0]))
# print(ll.sort012([1,1,2,2,0,1,2,2,1,0,1,2,0,2,1]))
# print(ll.target_sum_pair([12, 9 ,-48 ,100 ,43 ,84 ,74 ,86 ,34 ,-37 ,60 ,-29 ,44], 160))
# print(ll.pivot_in_sorted_rotated_array([9, 15, 16, 19, 21, 23, 24, 1, 2, 12]))
