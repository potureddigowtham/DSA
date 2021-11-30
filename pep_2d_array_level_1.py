class Solution:
    def matrix_mul(self):
        A = [[5, 5, 5],
             [6, 6, 6]]
        B = [[1, 2, 3, 4],
             [1, 2, 3, 4],
             [1, 2, 3, 4]]
        result = [[0, 0, 0, 0],
                  [0, 0, 0, 0]]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        print(result)

    def state_of_wakanda_1(self):
        a = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
        flag = 0
        for i in range(len(a[0])):
            if flag == 0:
                for j in range(len(a)):
                    print(a[j][i])
                    flag = 1
            else:
                for j in range(len(a)-1, -1, -1):
                    print(a[j][i])
                    flag = 0

    def spiral_matrix(self):
        a = [[11, 12, 13, 14, 15],
             [21, 22, 23, 24, 25],
             [31, 32, 33, 34, 35]]
        minr = minc = 0
        maxr, maxc = len(a)-1, len(a[0])-1
        total = len(a) * len(a[0])
        count = 0
        while(total > count):
            # left wall
            for i in range(minr, maxr):
                if total > count:
                    print(a[i][minc])
                    count += 1
            # down wall
            for j in range(minc, maxc):
                if total > count:
                    print(a[maxr][j])
                    count += 1
            # side wall
            for k in range(maxr, minr, -1):
                if total > count:
                    print(a[k][maxc])
                    count += 1
            # top wall
            for li in range(maxc, minc, -1):
                if total > count:
                    print(a[minr][li])
                    count += 1
            minr += 1
            minc += 1
            maxr -= 1
            maxc -= 1
        return

    def exit_point_of_matrix(self):
        a = [[0, 0, 1, 0],
             [1, 0, 0, 1],
             [0, 0, 0, 1],
             [1, 0, 0, 0]]
        print(len(a), len(a[0]))
        dir = 0
        i = j = 0
        while True:
            dir = (dir + a[i][j]) % 4
            print(i, j)

            if dir == 0:  # east
                print(dir, i, j)
                j += 1

            elif dir == 1:  # south
                print(dir, i, j)
                i += 1

            elif dir == 2:  # west
                print(dir, i, j)
                j -= 1

            elif dir == 3:  # south
                print(dir, i, j)
                i -= 1

            if i < 0:
                i += 1
                break
            elif i >= len(a):
                i -= 1
                break
            elif j < 0:
                j += 1
                break
            elif j >= len(a[0]):
                j -= 1
                break
        print(i, j)

    def array_rotate_by_90_degrees_transpose_reverse(self):
        # array = [['00', '01', '02', '03'],
        #          ['10', '11', '12', '13'],
        #          ['20', '21', '22', '23'],
        #          ['30', '31', '32', '33']]

        array = [['0', '1', '2', '3'],
                 ['4', '5', '6', '7'],
                 ['8', '9', '10', '11'],
                 ['12', '13', '14', '15']]

        for i in range(len(array)):
            for j in range(i+1, len(array)):
                if i < j:
                    array[i][j], array[j][i] = array[j][i], array[i][j]

        i = 0
        while i < len(array):
            j_start, j_end = 0, len(array)-1
            while j_start < j_end:
                array[i][j_start], array[i][j_end] = array[i][j_end], \
                    array[i][j_start]
                j_start += 1
                j_end -= 1
            i += 1
        print(array)

    def ring_rotate(self):
        # array = [['00', '01', '02', '03'],
        #          ['10', '11', '12', '13'],
        #          ['20', '21', '22', '23'],
        #          ['30', '31', '32', '33']]

        array = [['00', '01', '02', '03', '04', '05'],
                 ['10', '11', '12', '13', '14', '15'],
                 ['20', '21', '22', '23', '24', '25'],
                 ['30', '31', '32', '33', '34', '35'],
                 ['40', '41', '42', '43', '44', '45'],
                 ['50', '51', '52', '53', '54', '55']]

        n = len(array)
        s = 3
        r = 1
        while r != 0:
            i, j = s-1, s-1
            temp = array[i][j]
            while i < n - s:
                i += 1
                array[i][j], temp = temp, array[i][j]
            while j < n - s:
                j += 1
                array[i][j], temp = temp, array[i][j]
            while i > s-1:
                i -= 1
                array[i][j], temp = temp, array[i][j]
            while j > s-1:
                j -= 1
                array[i][j], temp = temp, array[i][j]
            r -= 1
        print(array)

    def state_of_wakanda_2(self):
        array = [['00', '01', '02', '03'],
                 ['10', '11', '12', '13'],
                 ['20', '21', '22', '23'],
                 ['30', '31', '32', '33']]

        for j in range(len(array[0])):
            i = 0
            k = j
            while k < len(array[0]):
                print(array[i][k])
                i += 1
                k += 1

    def saddle_point(self):
        mat = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

        n = len(mat)

        for i in range(n):
            min_row = mat[i][0]
            col_ind = 0
            for j in range(1, n):
                if (min_row > mat[i][j]):
                    min_row = mat[i][j]
                    col_ind = j
            k = 0
            for k in range(n):
                if (min_row < mat[k][col_ind]):
                    break
                k += 1
            if (k == n):
                print("Value of Saddle Point ", min_row)
                return True
        return False
  
    def search_in_sorted_2d_array(self, x):
        a = [[00, 1, 2],
             [10, 11, 12],
             [20, 21, 22]]
        i = 0
        j = len(a[0])-1

        if a[i][j] == x:
            return (i, j)

        while a[i][j] < x and i < len(a) - 1:
            i += 1
            if a[i][j] == x:
                return (i, j)
            
        while a[i][j] > x and j > 0:
            j -= 1
            if a[i][j] == x:
                return (i, j)

        return False

    def main(self):
        # self.matrix_mul()
        # self.state_of_wakanda_1()
        # self.spiral_matrix()
        # self.exit_point_of_matrix()
        # self.array_rotate_by_90_degrees_transpose_reverse()
        # self.ring_rotate()
        # self.state_of_wakanda_2()
        # self.saddle_point()
        print(self.search_in_sorted_2d_array(00))


if __name__ == '__main__':
    obj = Solution()
    obj.main()
