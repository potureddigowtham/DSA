class Solution:
    def __init__(self):
        pass

    def print_decresing(self, n):
        if n < 1:
            return
        print(n)
        self.print_decresing(n-1)

    def print_increasing(self, n):
        if n < 1:
            return
        self.print_increasing(n-1)
        print(n)

    def print_increasing_decreasing(self, n):
        if n < 1:
            return
        print(n)
        self.print_increasing_decreasing(n-1)
        print(n)

    def factorial(self, n):
        if n < 1:
            return 1
        return n * self.factorial(n-1)

    def power(self, x, n):
        if n < 1:
            return 1
        return x * self.power(x, n-1)

    def power_logarithmic(self, x, n):
        if n < 1:
            return 1
        ans = self.power_logarithmic(x, n//2) * self.power_logarithmic(x, n//2)
        if n % 2 != 0:
            ans *= x
        return ans

    def zigzag(self, n):
        if n < 1:
            return
        print(n)
        self.zigzag(n-1)
        print(n)
        self.zigzag(n-1)
        print(n)

    def tower_of_hanoi(self, n, a, b, c):
        if n <= 0:
            return
        self.tower_of_hanoi(n-1, a, c, b)
        print(n, a, b)
        self.tower_of_hanoi(n-1, c, b, a)

    def main(self):
        # self.print_decresing(5)
        # self.print_increasing(5)
        # self.print_increasing_decreasing(5)
        # print(self.factorial(5))
        # print(self.power(2, 5))
        # print(self.power_logarithmic(2, 5))
        # self.zigzag(5)
        # self.tower_of_hanoi(2, 'a', 'b', 'c')


if __name__ == "__main__":
    obj = Solution()
    obj.main()
