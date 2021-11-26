class pep_arrays_level_1():

    def span_of_array(self, array):
        max_number = array[0]
        min_number = array[0]
        for k in enumerate(array):
            if max_number < k:
                max_number = k
            if min_number > k:
                min_number = k
        return max_number-min_number

    def bar_chart(self, array):
        n = max(array)
        for i in range(n, 0, -1):
            line = ''
            for j in array:
                if i <= j:
                    line += "*\t"
                else:
                    line += "\t"
            print(line)

    def add_arrays(self, array1, array2):
        ans = ''
        carry = 0
        i = len(array1) - 1
        j = len(array2) - 1
        while i >= 0 or j >= 0:
            d = carry
            if i >= 0:
                d += array1[i]
            if j >= 0:
                d += array2[j]
            carry = d / 10
            ans += str(d % 10)

            i -= 1
            j -= 1
        if carry > 0:
            ans += str(carry)
        print(ans[::-1])

    def subtract_arrays(self, array1, array2):
        if len(array1) < len(array2):
            array1, array2 = array2, array1

        for i in range(len(array2), len(array1)):
            array2.insert(0, 0)
        ans = []
        carry = 0
        i = len(array1) - 1
        j = len(array2) - 1
        while i >= 0 or j >= 0:
            array1[i] = array1[i] - carry
            if array1[i] < array2[j] and i >= 0 and j >= 0:
                carry = 1
                ans.append((array1[i] + 10) - array2[j])
            else:
                carry = 0
                ans.append(array1[i] - array2[j])

            i -= 1
            j -= 1
        print(ans[::-1])

    def reverse_array(self, array):
        size = len(array)
        start = 0
        end = size-1
        while start+1 != end and start != end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
        print(array)
        return array

    def reverse_array_recursion_1(self, array, start, end):
        if not array:
            return array
        a, b = array[0], array[1:]
        return self.reverse_array_recursion(b) + [a]

    def reverse_array_recursion_2(self, array, start, end):
        if not array or start >= len(array)/2:
            return array
        array[start], array[end-1] = array[end-1], array[start]
        self.reverse_array_recursion(array, start+1, end-1)
        return array

    def reverse_array_recursion_3(self, array):
        if len(array) == 0:
            return []
        return [array[-1]] + self.reverse_array_recursion_3(array[:-1])

    def rotate_array(self, array, k):
        if k >= 0:
            k = len(array) - k
        else:
            k = len(array) + k
        return array[k:] + array[:k]

    def inverse_array(self, array):
        array2 = [0]*len(array)
        for i, k in enumerate(array):
            array2[k] = i
        return array2

    def print_sub_array(self, array):
        n = 0
        m = len(array) - 1
        while n <= m:
            line = ''
            for i, k in enumerate(array[n:]):
                line += str(k)
                print(line)
            n += 1

    def broken_economy(self, array, k):
        # if k in array:
        #     return k
        # else:
        #     for i, j in enumerate(array):
        #         if j > k:
        #             return j, array[i-1]

        low, high, ciel, floor = 0, len(array)-1, 0, 0
        while low <= high:
            mid = (low+high) / 2
            if k < array[mid]:
                high = mid - 1
                ciel = array[mid]
            elif k > array[mid]:
                low = mid + 1
                floor = array[mid]
            else:
                print(array[mid])
                return array[mid]
        print(ciel, floor)


if __name__ == "__main__":
    obj = pep_arrays_level_1()
    # print(obj.span_of_array([15,30,40,4,11,9]))
    # obj.bar_chart([3,1,0,7,5])
    # obj.add_arrays([9, 9, 9], [1])
    # obj.subtract_arrays([9, 9, 9, 9], [3, 3, 3, 3, 3, 3])
    # print(obj.reverse_array([0, 1, 2, 3, 4, 5]))
    # print(obj.reverse_array_recursion_1([0, 1, 2, 3, 4, 5]))
    # print(obj.reverse_array_recursion_2([0, 1, 2, 3, 4, 5], 0, 6))
    # print(obj.reverse_array_recursion_3([0, 1, 2, 3, 4, 5]))
    # print(obj.rotate_array([1, 2, 3, 4, 5], -3))
    # print(obj.inverse_array([4, 5, 2, 0, 1, 3]))
    # obj.print_sub_array([1, 2, 3])
    obj.broken_economy([1, 5, 10, 15, 22, 33, 40, 42, 55, 66], 22)
