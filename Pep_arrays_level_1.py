class Solution:
    def digit_frequency(self, n, d):
        counter = 0
        while n:
            dig = n % 10
            n = n // 10
            if d == dig:
                counter += 1
        print(counter)

    def decimal_to_anybase(self, number, base):
        answer = 0
        counter = 0
        while number:
            answer += (number % base) * (pow(10, counter))
            counter += 1
            number = number // base
        print(answer)

    def anybase_to_decimal(self, number, base):
        decimal = 0
        counter = 0
        while number:
            decimal += (number % 10) * (pow(2, counter))
            counter += 1
            number = number // 10
        print(decimal)
        

if __name__ == '__main__':
    obj = Solution()
    # obj.digit_frequency(994543234, 4)
    # obj.decimal_to_anybase(57, 2)
    # obj.anybase_to_decimal(111001, 2)
