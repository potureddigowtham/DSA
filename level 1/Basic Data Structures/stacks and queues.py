from json.tool import main


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

    def prefix_evaluation_conversion(self, exp):
        ans = []
        inf = []
        post = []
        for i in exp[::-1]:
            if i in ["+", "-", "*", "/"]:
                o = i
                v1 = ans.pop()
                v2 = ans.pop()
                ans.append(self.operation(int(v1), int(v2), o))

                v1 = inf.pop()
                v2 = inf.pop()
                inf.append("("+v1+o+v2+")")

                v1 = post.pop()
                v2 = post.pop()
                post.append(v1+v2+o)
            else:
                ans.append(i)
                inf.append(i)
                post.append(i)
        return ans, inf, post

    def celebrity(self, arr):
        n = len(arr)
        stack = []
        for i in range(len(arr)):
            stack.append(i)
        while len(stack) != 2:
            e1 = stack.pop()
            e2 = stack.pop()
            if arr[e1][e2] == 1:
                stack.append(e2)
            else:
                stack.append(e1)

        pot = stack.pop()
        for i in range(len(arr)):
            if i != pot:
                if arr[i][pot] == 0 or arr[pot][i] == 1:
                    return None
        return pot

    def merge_overlapping_interval(self, arr):
        arr.sort()
        stack = []
        stack.append(arr[0])
        for i in range(1, len(arr)):
            narr = arr[i]
            if stack[-1][1] >= narr[0]:
                stack[-1][1] = narr[1]
            else:
                stack.append(narr)
        return stack

    def smallest_number_following_pattern(self, pattern):
        stack = []
        n = 1
        for i in pattern:
            if i == "d":
                stack.append(n)
                n += 1
            else:
                stack.append(n)
                n += 1
                while len(stack) != 0:
                    print(stack.pop())
        stack.append(n)
        if stack:
            while len(stack) != 0:
                print(stack.pop())


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
    # print(obj.prefix_evaluation_conversion("-+2/*6483"))
    # a = [ [0, 1, 1, 1],
    #       [1, 0, 1, 0],
    #       [0, 0, 0, 0],
    #       [1, 1, 1, 0]]
    # print(obj.celebrity(a))
    # b = [[22, 28], [1, 8], [25, 27], [14, 19], [27, 30], [5, 12]]
    # print(obj.merge_overlapping_interval(b))
    # obj.smallest_number_following_pattern("ddidddid")

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        return self.stack

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    a = Stack()
    # a.push(10)
    # a.push(20)
    # a.pop()
    # a.size()
    # a.peek()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        return self.queue

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    a = Queue()
    a.enqueue(10)
    a.enqueue(20)
    a.dequeue()
    a.size()
    a.peek()
