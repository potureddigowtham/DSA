class Solution:

    def flood_fill(self, arr, r, c, ans, visited, n, m):
        if r < 0 or c < 0 or r == n or c == m or arr[r][c] == 1 or visited[r][c] == True:
            return

        if r == n-1 and c == m-1:
            print(ans)
            return
            
        visited[r][c] = True
        self.flood_fill(arr, r+1, c, ans+"d", visited, n, m)
        self.flood_fill(arr, r, c+1, ans+"r", visited, n, m)
        self.flood_fill(arr, r-1, c, ans+"t", visited, n, m)
        self.flood_fill(arr, r, c-1, ans+"l", visited, n, m)
        visited[r][c] = False

    def target_sum_subsets(self, arr, idx, ans, sos, tar):
        if sos > tar:
            return

        if idx == len(arr):
            if sos == tar:
                print(ans+" . ")
            return

        self.target_sum_subsets(arr, idx+1, ans+str(arr[idx])+",", sos + arr[idx], tar)
        self.target_sum_subsets(arr, idx+1, ans, sos, tar)


    def main(self):
        # arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # arr = [[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 0],
        #        [0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 0, 1, 1],
        #        [1, 0, 1, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0]]
        # visited = []
        # for i in arr:
        #     temp = []
        #     for j in i:
        #         temp.append(False)
        #     visited.append(temp)
        # self.flood_fill(arr, 0, 0, "", visited, len(arr), len(arr[0]))
        self.target_sum_subsets([1, 2, 3, 4, 5], 0, "", 0, 6)


if __name__ == "__main__":
    obj = Solution()
    obj.main()
