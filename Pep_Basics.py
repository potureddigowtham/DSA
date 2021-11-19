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

    def febonacci(self, n):
        # Recurssion
        if number < 0: return 
        if number <= 1: return number
        return self.febonacci(number-1)+self.febonacci(number-2)
        # Iteration
        # f = [0, 1]
        # for i in range(2, n+1):
        #     f.append(f[i-1] + f[i-2])
        # return f[n]


if __name__ == '__main__':
    obj = Basics()
    # obj.Z(5)
    # for i in range(0,100):
    #     obj.isPrime(i)
    # print(obj.febonacci(9))

    