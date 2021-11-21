from math import sqrt

class Basics():
    def Z(self,end):
        ans = ''
        for row in range(end+1):
            for col in range(end+1):
                if ((row == 0 or row == end) and col > 0 and col < end or row+col == end):
                    ans = ans+"*"
                else:
                    ans = ans+"_"
            ans = ans+"\n"
        print(ans)

    def isPrime(self,number):
        if number <= 0:
            return 

        for i in range(2,int(sqrt(number)+1)):
            if number % i == 0:
                return
        print(str(number) + " Prime ")

    def febonacci(self, number):
        # Recurssion
        if number < 0: return 
        if number <= 1: return number
        return self.febonacci(number-1)+self.febonacci(number-2)
        # Iteration
        # f = [0, 1]
        # for i in range(2, n+1):
        #     f.append(f[i-1] + f[i-2])
        # return f[n]

    def countDigits(self, number):
        count = 0
        while number != 0:
            number = number // 10
            count += 1
        return count

    def printDigits(self, number):
        while number != 0:
            print(number%10)
            number /= 10
        return 

    def reverseNumber(self, number):
        ans = ""
        while number != 0:
            ans = ans + str(number%10)
            number /= 10
        return int(ans) 

    def inverseNumber(self, number):
        position = 0
        ans = 0
        while number != 0:
            position += 1
            ans = ans + position * pow(10, (number % 10) - 1)
            number = number // 10
        return ans

    def rotateNumber(self, N, K):
        X = self.countDigits(N)
        K = ((K % X) + X) % X
        left_no = N // pow(10, X - K)
        N = N % pow(10, X - K)
        left_digit = self.countDigits(left_no)
        N = N * pow(10, left_digit) + left_no
        print(N)

    def gcd(self, n1, n2):
        if n1 == 0:
            return n2
        return self.gcd(n2 % n1, n1)

    def lcm(self, n1, n2):
        lcm = (n1 * n2) / self.gcd(n1, n2)
        return lcm

    def primeFactors(self, number):
        for i in range(2,number):
            while number % i == 0:
                print(i)
                number = number / i
            if number == 1:
                return

if __name__ == '__main__':
    obj = Basics()
    obj.Z(5)
    for i in range(0,100):
        obj.isPrime(i)
    print(obj.febonacci(9))
    print(obj.countDigits(89024234))
    obj.printDigits(89024234)
    print(obj.reverseNumber(123))
    print(obj.inverseNumber(24153))
    print(obj.rotateNumber(12345, -2))
    print(obj.gcd(36, 24))
    print(obj.lcm(36, 24))
    obj.primeFactors(1440)