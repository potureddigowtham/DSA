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
        return answer

    def anybase_to_decimal(self, number, base):
        # decimal = 0
        # counter = 0
        # while number:
        #     decimal += (number % 10) * (pow(base, counter))
        #     counter += 1
        #     number = number // 10
        # return decimal

        decimal = 0
        p = 1
        while number:
            decimal += (number % 10) * p
            p = p * base
            number = number // 10
        return decimal

    def anybase_to_anybase(self, number, basefrom, baseto):
        decimal = self.anybase_to_decimal(number, basefrom)
        answer = self.decimal_to_anybase(decimal, baseto)
        return answer

    def any_base_addition(self, base, number1, number2):
        answer = 0
        carry = 0
        p = 1
        while number1 > 0 or number2 > 0 or carry > 0:
            digit1 = (number1 % 10)
            digit2 = (number2 % 10)
            number1 = number1 // 10
            number2 = number2 // 10

            digit = digit1 + digit2 + carry
            carry = digit / base
            digit = digit % base
            
            answer += digit * p
            p = p * 10
        return answer

    def any_base_substraction(self, base, number1, number2):
        if number2 >= number1:
            number1, number2 = number2, number1
        p = 1
        answer = 0
        carry = 0
        while number1 > 0 or number2 > 0 or carry == -1:
            digit1 = number1 % 10
            digit2 = number2 % 10 
            number1 = number1 / 10
            number2 = number2 / 10

            digit = 0
            digit1 = digit1 + carry
            if digit1 >= digit2:
                carry = 0
                digit = digit1 - digit2
            else:
                carry = -1
                digit = (digit1 + base) - digit2
            answer += digit * p
            p = p * 10
        return answer

    def any_base_multiplication(self, base, number1, number2):
        pass

if __name__ == '__main__':
    obj = Solution()
    # obj.digit_frequency(994543234, 4)
    # print(obj.decimal_to_anybase(57, 3))
    # print(obj.anybase_to_decimal(1110010, 2))
    # print(obj.anybase_to_anybase(111001, 2, 3))
    # print(obj.any_base_addition(2, 1, 1))
    # print(obj.any_base_substraction(7, 21, 202))
    # print(obj.any_base_multiplication(base, number1, number2))


