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

    def pattern9(self, n):
        for i in range(1, n):
            line = ''
            for j in range(1, n):
                if i+j == n and i != j:
                    line += "*    "
                elif i==j:
                    line += "*    "
                else:
                    line += "     "
            print(line)

    def pattern10(self, n):
        o_ = n/2
        i_ = -1
        for i in range(1, n+1):
            line = ''
            for j in range(1, o_+1):
                line += ("\t")
            line += ("*\t")
            for k in range(1, i_+1):
                line += ("\t")
            if i > 1 and i < n:
                line += ("*\t")
            if i <= n/2:
                o_ -= 1
                i_ += 2
            else:
                o_ += 1
                i_ -= 2
            print(line)

    def pattern11(self, n):
        number = 1
        for i in range(1, n+1):
            line = ''
            for j in range(1, n+1):
                if j <= i:
                    if number < 10:
                        line += str(number)+"\t\t"
                    else:
                        line += str(number)+"\t"
                    number += 1
            print(line)

    def pattern12(self, n):
        a = 0
        b = 1
        for i in range(1, n+1):
            line = ''
            for j in range(1, i+1):
                line += str(a)+"\t"
                c = a+b
                a = b
                b = c
            print(line)

    def pattern13(self, n):
        for i in range(0, n+1):
            line = ''
            icj = 1
            for j in range(0, i+1):
                line += str(icj)+"\t"
                icjp1 = (icj * (i - j))/ (j+1)
                icj = icjp1
            print(line)

    def pattern14(self, n):
        for i in range(1, 11):
            line = str(n) + " x " + str(i) + " = " + str(n*i) 
            print(line)

    def pattern15(self, n):
        _ = n//2
        star = 1
        value  = 1
        for i in range(1, n+1):
            line = ''
            cval = value
            for j in range(_):
                line += (" \t")
            for k in range(star):
                line += str(cval)+("\t")
                if k < star //2 :
                    cval += 1
                else:
                    cval -= 1
            if i <= (n // 2):
                _ -= 1
                star += 2            
                value += 1
            else:
                _ += 1
                star -=2
                value -= 1
            print(line) 

    def pattern16(self, n):
        star = 1
        _ = 2*n - 3
        for i in range(1, n+1):
            value = 1
            line = ''
            for j in range(star):
                line +=  str(value)+"\t"
                value += 1
            
            for k in range(_):
                line += "\t"

            if i == n:
                value -= 1
                star -= 1
            for l in range(star):
                value -= 1
                line += str(value)+"\t"

            star += 1
            _ -= 2
            print(line)

    def pattern17(self, n):
        _ = 2
        star = 1
        for i in range(1, n+1):
            line = ''

            for j in range(_):
                if i == n // 2 + 1:
                    line += "*\t"
                else:
                    line += "\t"

            for k in range(star):
                line += "*\t"

            if i <= n//2:
                star += 1
            else:
                star -= 1
            print(line)

    def pattern18(self, n):
        for i in range(1, n+1):
            line = ''
            for j in range(1, n+1):
                if i == 1 or i == n or i == j or i+j == n+1:
                    line += "*\t"
                elif i > n // 2 and i + j > n and j < i:
                    line += "*\t"
                else:
                    line += "\t"

            print(line)

    def pattern19(self, n):
        for i in range(1, n+1):
            line = ''
            for j in range(1, n+1):
                if i == 1:
                    if j == n or j <= n // 2 + 1:
                        line += "*\t"
                    else:
                        line += "\t"

                elif i <= n // 2:
                    if j == n or j == n // 2 + 1:
                        line += "*\t"
                    else:
                        line += "\t"

                elif i == n // 2 + 1:
                    line += "*\t"

                elif i < n:
                    if j == 1 or j == n // 2 + 1:
                        line += "*\t"
                    else:
                        line += "\t"

                else:
                    if j == 1 or j >= n // 2 + 1:
                        line += "*\t"
                    else:
                        line += "\t"
            print(line)

    def pattern20(self, n):
        for i in range(1, n+1):
            line = ""
            for j in range(1, n+1):
                if j == 1 or j == n:
                    line += "*\t"
                elif i >= n // 2 + 1:
                    if i + j == n+1 or i == j:
                        line += "*\t"
                    else:
                        line += "\t"
                else:
                    line += "\t"
            print(line)


if __name__ == '__main__':
    obj = Solution()
    # obj.pattern1(5)
    # obj.pattern2(5)
    # obj.pattern3(5)
    # obj.pattern4(5)  
    # obj.pattern5(5)  
    # obj.pattern6(5)  
    # obj.pattern7(5)  
    # obj.pattern8(5)  
    # obj.pattern9(6) 
    # obj.pattern10(5)
    # obj.pattern11(5)
    # obj.pattern12(5)
    # obj.pattern13(5)
    # obj.pattern14(10)
    # obj.pattern15(5)
    # obj.pattern16(4)
    # obj.pattern17(5)
    # obj.pattern18(7)
    # obj.pattern19(7)
    # obj.pattern20(5)
