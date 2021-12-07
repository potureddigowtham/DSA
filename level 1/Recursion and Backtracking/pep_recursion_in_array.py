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

    def first_index(self, arr, id, n):
        if id > len(arr)-1:
            return
        self.first_index(arr, id+1, n)
        if arr[id] == n:
            print(id)
            return id

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
        # self.first_index([8000, 500], 0, 500)
        # print(self.last_index([40, 20, 30], 0, 10))
        print(self.all_index([10, 10, 10], 0, 10, []))


if __name__ == "__main__":
    obj = Solution()
    obj.main()
