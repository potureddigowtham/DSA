class Solution:

    def display_array(self, arr, id):
        if id > len(arr)-1:
            return
        print(arr[id])
        self.display_array(arr, id+1)

    def display_array_reverse(self, arr, id):
        if id > len(arr)-1:
            return
        self.display_array_reverse(arr, id+1)
        print(arr[id])

    def max_of_array(self, arr, id):
        if id > len(arr)-1:
            return
        maxi = max(arr[id], self.max_of_array(arr, id+1))
        return maxi

    def first_index(self, arr, id, n):  # ignore
        if id > len(arr)-1:
            return -1
        self.first_index(arr, id+1, n)
        if arr[id] == n:
            print(id)
            return id

    def first_occurance_1(self, n, x, index, ans):
        if len(n) <= 0:
            ans = -1
            return ans
        if x == n[0]:
            ans = index
            return ans
        ans = self.first_occurance_1(n[1:], x, index+1, ans)
        return ans

    def last_index(self, arr, id, n):
        if id > len(arr)-1:
            return -1
        liisa = self.last_index(arr, id+1, n)
        if liisa == -1:
            if arr[id] == n:
                return id
            else:
                return -1
        else:
            return liisa

    def all_index(self, arr, id, n, a):
        if id > len(arr)-1:
            return
        if arr[id] == n:
            print(id)
            a.append(id)
        self.all_index(arr, id+1, n, a)
        return a

    def main(self):
        # self.display_array([10, 20, 30, 40, 50], 0)
        # self.display_array_reverse([10, 20, 30, 40, 50], 0)
        # print(self.max_of_array([1000, 60, 30, 8000, 500], 0))
        self.first_index([15, 11, 40, 4, 4, 9], 0, 4)
        print(self.first_occurance_1([140, 4, 4, 10], 14, 0, 0))
        # print(self.last_index([40, 20, 30], 0, 10))
        # print(self.all_index([10, 10, 10], 0, 10, []))


if __name__ == "__main__":
    obj = Solution()
    obj.main()
