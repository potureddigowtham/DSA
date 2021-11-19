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

if __name__ == '__main__':
    obj = Basics()
    # obj.Z(5)
    # for i in range(0,100):
    #     obj.isPrime(i)

    