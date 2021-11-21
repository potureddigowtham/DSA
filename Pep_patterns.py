class Solution:

    def pattern1(self, n):
        for i in range(1, n+1):
            line = ''
            for j in range(1, i+1):
                line += '*    '
            print(line)

    def pattern2(self, n):
        for i in range(n, 0, -1):
            line = ''
            for j in range(1, i+1):
                line += '*    '
            print(line)

    def pattern3(self, n):
        for i in range(1, n+1):
            line = ''
            for j in range(1, n+1):
                if i+j >= n+1:
                    line += '*    '
                else:
                    line += '      '
            print(line)

    def pattern4(self, n):
        for i in range(1, n+1):
            line = ''
            for j in range(1, n+1):
                if j >= i:
                    line += '*    '
                else:
                    line += '     '
            print(line)

    def pattern5(self, n):
        _ = n/2
        star = 1
        for i in range(1, n+1):
            line = ""
            for j in range(_):
                line += "     "
            for k in range(star):
                line += "*    "
            if i <= n/2:
                _ -= 1
                star += 2
            else:
                _ += 1
                star -= 2
            print(line)

    def pattern6(self, n):
        star = n/2 + 1
        _ = 1
        for i in range(1, n+1):
            line = ""
            for k in range(star):
                line += "*    "
            for j in range(_):
                line += "     "
            for l in range(star):
                line += "*    "
            if i <= n/2:
                star -= 1
                _ += 2
            else:
                star += 1
                _ -= 2
            print(line) 

    def pattern7(self, n):
        for i in range(n+1):
            line = ''
            for j in range(n+1):
                if i==j:
                    line += "*    "
                else:
                    line += "     "
            print(line)

    def pattern8(self, n):
        for i in range(n+1):
            line = ''
            for j in range(n+1):
                if i+j == n:
                    line += "*    "
                else:
                    line += "     "
            print(line)

if __name__ == '__main__':
    obj = Solution()
    # obj.pattern1(5)s
    # obj.pattern2(5)
    # obj.pattern3(5)
    # obj.pattern4(5)  
    # obj.pattern5(5)  
    # obj.pattern6(5)  
    # obj.pattern7(5)  
    obj.pattern8(5)  