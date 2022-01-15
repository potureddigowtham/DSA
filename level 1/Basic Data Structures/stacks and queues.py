class Solution:
    def DuplicateBracket(self, exp):
        stack = []
        for i in exp:
            if i == ")":
                if stack[-1] == "(":
                    return True
                else:
                    while stack[-1] != "(":
                        stack.pop()
                    stack.pop()
            else:
                stack.append(i)
            print(stack)
        return False

    def validate(self, stack, char):
        if len(stack) == 0:
            return False
        elif stack[-1] != char:
            return False
        else:
            stack.pop()

    def BalancedBracket(self, exp):
        stack = []
        for i in exp:
            if i in ["[","(","{"]:
                stack.append(i)
            elif i == "]":
                det = self.validate(stack, "[")
            elif i == ")":
                det = self.validate(stack, "(")
            elif i == "}":
                det = self.validate(stack, "{")
            print(stack)
        if len(stack) == 0 and det != False:
            return True
        else:
            return False

    def NextGreaterElementToTheRight(self, arr):
        stack = []
        ans = [-1]*len(arr)
        stack.append(arr[len(arr)-1])
        for i in range(len(arr)-2, -1, -1):
            while len(stack) > 0:
                if arr[i] > stack[-1]:
                    stack.pop()
                else:
                    break
            ans[i] = stack[-1] if len(stack) > 0 else -1
            stack.append(arr[i])
            print(stack)
            print(ans)

    def stock_span_without_stack(self, arr):
        ans = [0]*len(arr)
        for i in range(len(arr)):
            val = 0
            idx = i
            while arr[i] >= arr[idx] and idx >= 0:
                val += 1
                idx -= 1
            ans[i] = val
        print(ans)

    def stock_span(self, arr):
        pass

    def largest_area_histogram(self, arr):
        stack = []
        ans = [0]*len(arr)
        for i in range(len(arr)):
            stack.append(arr[i])
            l = arr[i]
            b = 1
            idx = i+1
            if idx <= len(arr)-1:
                while stack[-1] <= arr[idx]:
                    b += 1
                    if idx < len(arr)-1:
                        idx += 1
                    else:
                        break
            idx1 = i-1
            if idx1 >= 0:
                while stack[-1] <= arr[idx1]:
                    b += 1
                    if idx1 > 0:
                        idx1 -= 1
                    else:
                        break
            ans[i] = l*b
            print(ans)
        return max(ans)

    def sliding_window_maximum(self, arr):
        stack = []
        ans = [0]*(len(arr)-3)
        for i in range(len(arr)-3):
            stack.append(arr[i])
            idx = i+1
            maxi = arr[i]
            while idx <= i+3:
                maxi = max(maxi, arr[idx])
                idx += 1
            ans[i] = maxi
            print(ans)

            
if __name__ == "__main__":
    obj = Solution()
    # print(obj.DuplicateBracket("(a+b)+(c+d)"))
    # print(obj.BalancedBracket("{[(a+b)+{(c+d)}]}["))
    # print(obj.NextGreaterElementToTheRight([2, 5, 9, 3, 1, 12, 6, 8, 7]))
    print(obj.stock_span([2, 5, 9, 3, 1, 12, 6, 8, 7]))
    # print(obj.largest_area_histogram([6,2,5,4,5,1,6]))
    # print(obj.sliding_window_maximum([2, 9, 3, 8, 1, 7, 12, 6, 14, 4, 32, 0, 7, 19, 8, 12, 6]))
