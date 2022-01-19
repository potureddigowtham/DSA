from ast import operator


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

    def infix_evaluation(self, exp):
        num = []
        ope = []
        for i in exp:
            if i.isdigit():
                num.append(int(i))
            elif i == "(":
                ope.append(i)
            elif i == ")":
                while ope[-1] != "(":
                    o = ope.pop()
                    v2 = num.pop()
                    v1 = num.pop()
                    num.append(self.operation(v1, v2, o))
                ope.pop()
            elif i in ["+", "-", "*", "/"]:
                while len(ope) != 0 and ope[-1] != "(" and self.precedence(i) <= self.precedence(ope[-1]):
                    o = ope.pop()
                    v2 = num.pop()
                    v1 = num.pop()
                    num.append(self.operation(v1, v2, o))
                ope.append(i)
        while len(num) > 1:
            o = ope.pop()
            v2 = num.pop()
            v1 = num.pop()
            ans = self.operation(v1, v2, o)
            num.append(ans)
        return ans


    def operation(self, v1, v2, o):
        if o == "+":
            return v1+v2
        elif o == "-":
            return v1-v2
        elif o == "*":
            return v1*v2
        elif o == "/":
            return v1/v2
        
    def precedence(self, o):
        if o == "+":
            return 1
        elif o == "-":
            return 1
        elif o == "*":
            return 2
        elif o == "/":
            return 2

    def infix_conversion(self, exp):
        pre = []
        post = []
        ope = []
        for i in exp:
            if i == "(":
                ope.append(i)
            elif i == ")":
                while ope[-1] != "(":
                    o = ope.pop()
                    v2 = pre.pop()
                    v1 = pre.pop()
                    pre.append(o+v1+v2)
                    v2 = post.pop()
                    v1 = post.pop()
                    post.append(v1+v2+o)
                ope.pop()
            elif i in ["+", "-", "*", "/"]:
                while len(ope) != 0 and ope[-1] != "(" and self.precedence(i) <= self.precedence(ope[-1]):
                    o = ope.pop()
                    v2 = pre.pop()
                    v1 = pre.pop()
                    pre.append(o+v1+v2)
                    v2 = post.pop()
                    v1 = post.pop()
                    post.append(v1+v2+o)
                ope.append(i)
            else:
                pre.append(i)
                post.append(i)
        while len(pre) > 1 or len(post) > 1:
            o = ope.pop()
            v2 = pre.pop()
            v1 = pre.pop()
            pre.append(o+v1+v2)
            v2 = post.pop()
            v1 = post.pop()
            post.append(v1+v2+o)
        return pre, post

    def postfix_evaluation_conversion(self, exp):
        ans = []
        inf = []
        pre = []
        for i in exp:
            if i in ["+", "-", "*", "/"]:
                o = i
                v2 = ans.pop()
                v1 = ans.pop()
                ans.append(self.operation(int(v1), int(v2), o))

                v2 = inf.pop()
                v1 = inf.pop()
                inf.append("("+v1+o+v2+")")

                v2 = pre.pop()
                v1 = pre.pop()
                pre.append(o+v1+v2)
            else:
                ans.append(i)
                inf.append(i)
                pre.append(i)
        return ans, inf, pre


            
if __name__ == "__main__":
    obj = Solution()
    # print(obj.DuplicateBracket("((a+b))+(c+d)"))
    # print(obj.BalancedBracket("{[(a+b)+{(c+d)}]}["))
    # print(obj.NextGreaterElementToTheRight([2, 5, 9, 3, 1, 12, 6, 8, 7]))
    # print(obj.stock_span([2, 5, 9, 3, 1, 12, 6, 8, 7]))
    # print(obj.largest_area_histogram([6,2,5,4,5,1,6]))
    # print(obj.sliding_window_maximum([2, 9, 3, 8, 1, 7, 12, 6, 14, 4, 32, 0, 7, 19, 8, 12, 6]))
    # print(obj.infix_evaluation("2+5-3*6/2"))
    # print(obj.infix_conversion("a*(b-c+d)/e"))
    # print(obj.postfix_evaluation_conversion("264*8/+3-"))
