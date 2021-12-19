class Solution:

    def fibanaci_dp(self, x, data):
        if x == 1 or x == 0:
            return x

        if x in data:  # memoization
            return data[x]

        ans = self.fibanaci_dp(x-1, data) + self.fibanaci_dp(x-2, data)
        data[x] = ans  # adding to memo
        return ans

    def climb_stairs_dp(self, n, dictionary):
        if n == 0:
            return 1
        elif n < 0:
            return 0

        if n in dictionary:  # memoization
            return dictionary[n]

        step_one = self.climb_stairs_dp(n-1, dictionary)
        step_two = self.climb_stairs_dp(n-2, dictionary)
        step_three = self.climb_stairs_dp(n-3, dictionary)
        total = step_one + step_two + step_three
        dictionary[n] = total  # adding to memo
        return total

    def climb_stair_with_jump_dp(self, n, arr, dp):
        for i in range(n-1, -1, -1):
            if i == n-1:
                dp[n] = 1
            for j in range(1, arr[i]+1):
                if i+j < len(dp):
                    dp[i] += dp[i+j]
        print(dp)
        return dp[0]

    def climb_stair_with_minimum_jump_dp(self, n, arr, dp):
        for i in reversed(range(0, n + 1)):
            if(i == n):
                dp[i] = 0
                continue

            minvalue = 30
            j = 1
            while (j <= arr[i] and (i + j) <= n):
                f = dp[i + j] + 1
                minvalue = min(f, minvalue)
                j += 1
            dp[i] = minvalue
        return dp[0]

    def min_cost_maze_travel_dp(self, arr, i, j, ans, sum, values):  # via recursion
        if i == len(arr)-1 and j == len(arr[0])-1:
            values[sum] = ans
            return
        elif i == len(arr) or j == len(arr):
            return

        self.min_cost_maze_travel_dp(arr, i+1, j, ans+"h", sum+arr[i][j], values)
        self.min_cost_maze_travel_dp(arr, i, j+1, ans+"v", sum+arr[i][j], values)
        return values[min(values)]

    def min_cost_maze_travel_dp(self, arr, dp):  # via iterrative and tabularization
        for i in reversed(range(len(arr))):
            for j in reversed(range(len(arr[0]))):
                if i == len(arr)-1 and j == len(arr[0])-1:
                    dp[i][j] = arr[i][j]
                elif i == len(arr)-1:
                    dp[i][j] = dp[i][j+1] + arr[i][j]
                elif j == len(arr[0])-1:
                    dp[i][j] = dp[i+1][j] + arr[i][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + arr[i][j]
        print(dp)
        return (dp[0][0])

    def goldmine_dp(self, arr, dp):
        n = len(arr)
        m = len(arr[0])
        for j in reversed(range(n)):
            for i in reversed(range(m)):
                if j == m-1:
                    dp[i][j] = arr[i][j]
                elif i == 0:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j+1]) + arr[i][j]
                elif i == n-1:
                    dp[i][j] = max(dp[i][j+1], dp[i-1][j+1]) + arr[i][j]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i-1][j+1], dp[i+1][j+1]) + arr[i][j]

        return (max(dp)[0])

    def array_rotate_helper(self, arr, lenght):
        return arr[lenght:]+arr[0:lenght]

    def target_sum_subsets_dp(self, arr, dp, target):
        for i in range(len(arr)+1):
            for j in range(target+1):
                if i == j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                elif j == 0:
                    dp[i][j] = True
                else:
                    if dp[i-1][j] is True:
                        dp[i][j] = True
                    else:
                        val = arr[i-1]
                        if j >= val:
                            if dp[i-1][j-val] is True:
                                dp[i][j] = True                
        return dp[len(arr)][len(dp[0])-1]

    def coin_change_combination_dp(self, arr, dp, amt):
        dp[0] = 1
        for i in arr:
            for j in range(i, amt+1):
                if i <= j:
                    dp[j] += dp[j-i]

        print(dp)
        print(dp[amt])

    def coin_change_permutations_dp(self, arr, dp, amt):
        dp[0] = 1
        for i in range(len(dp)):
            for j in arr:
                if i >= j:
                    dp[i] += dp[i - j]
        print(dp)
        print(dp[amt])

    def zero_one_knapsack_dp(self, arr1, arr2, target, dp):
        for i in range(len(arr1)+1):
            for j in range(target+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif (arr1[i-1] <= j):
                    dp[i][j] = max(arr2[i-1]+dp[i-1][j - arr1[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        print(dp[-1][-1])

    def zero_one_knapsack_unbounded_dp_1(self, arr1, arr2, target, dp):
        for i in range(len(dp)):
            maxi = 0
            for k, j in enumerate(arr1):
                if j <= i:
                    maxi = max(maxi, arr2[k]+dp[i-j])
            dp[i] = maxi
        print(dp)

    def zero_one_knapsack_unbounded_dp_2(self, arr1, arr2, target, dp):
        for i in range(len(arr1)+1):
            for j in range(target+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif (arr1[i-1] <= j):
                    dp[i][j] = max(arr2[i-1]+dp[i-1][j - arr1[i-1]], dp[i-1][j], arr2[i-1]+dp[i][j-arr1[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        print(dp[-1][-1])
 
    def main(self):
        # print(self.fibanaci_dp(3, {}))
        # print(self.climb_stairs_dp(4, {}))

        # n = 10
        # arr = [3, 2, 4, 2, 0, 2, 3, 1, 2, 2]
        # dp = [0] * (n + 1)
        # print(self.climb_stair_with_jump_dp(n, arr, dp))
        # print(self.climb_stair_with_minimum_jump_dp(n, arr, dp))

        # arr = [[1, 2, 3],
        #        [4, 7, 6],
        #        [1, 3, 1]]
        # print(self.min_cost_maze_travel_dp(arr, 0, 0, "", arr[0][0], {}))  #via recursion

        # dp = []
        # for i in range(len(arr)):
        #     dp_c = [0] * len(arr[0])
        #     dp.append(dp_c)
        # # print(self.min_cost_maze_travel_dp(arr, dp))

        # print(self.goldmine_dp(arr, dp))

        # arr = [4, 2, 7, 1, 3]
        # target = 10
        # dp = []
        # for i in range(len(arr)+1):
        #     temp = [0] * (target + 1)
        #     dp.append(temp)
        # print(self.target_sum_subsets_dp(arr, dp, target))

        # arr = [2, 3, 5, 6]
        # amt = 10
        # dp = [0] * (amt+1)
        # self.coin_change_combination_dp(arr, dp, amt)

        # arr = [2, 3, 5, 6]
        # amt = 7
        # dp = [0] * (amt + 1)
        # self.coin_change_permutations_dp(arr, dp, amt)

        arr1 = [2, 5, 1, 3, 4]
        arr2 = [15, 14, 10, 45, 30]
        target = 7
        dp = []
        for i in range(len(arr1)+1):
            temp = []
            for j in range(target+1):
                temp.append(0)
            dp.append(temp)
        self.zero_one_knapsack_dp(arr1, arr2, target, dp)

        # arr1 = [2, 5, 1, 3, 4]
        # arr2 = [15, 14, 10, 45, 30]
        # target = 7
        # dp = [0] * (target+1)
        # self.zero_one_knapsack_unbounded_dp_1(arr1, arr2, target, dp)

        # arr1 = [2, 5, 1, 3, 4]
        # arr2 = [15, 14, 10, 45, 30]
        # target = 7
        # dp = []
        # for i in range(len(arr1)+1):
        #     temp = []
        #     for j in range(target+1):
        #         temp.append(0)
        #     dp.append(temp)
        # self.zero_one_knapsack_unbounded_dp_2(arr1, arr2, target, dp)


if __name__ == "__main__":
    obj = Solution()
    obj.main()
