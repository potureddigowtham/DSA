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



if __name__ == "__main__":
    obj = Solution()
    # print(obj.DuplicateBracket("(a+b)+(c+d)"))
    print(obj.BalancedBracket("{[(a+b)+{(c+d)}]}["))