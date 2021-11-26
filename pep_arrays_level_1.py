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


if __name__ == "__main__":
    obj = pep_arrays_level_1()
    # print(obj.span_of_array([15,30,40,4,11,9]))
    # obj.bar_chart([3,1,0,7,5])
    # obj.add_arrays([9, 9, 9], [1])
    obj.subtract_arrays([9, 9, 9, 9], [3, 3, 3, 3, 3, 3])
