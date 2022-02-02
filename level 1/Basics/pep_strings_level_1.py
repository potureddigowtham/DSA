class Solution:

    def palindrome(self, s):
        flag = 0
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def substrings(self, s):
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.palindrome(s[i:j]):
                    print(s[i:j])

    def string_compression(self, s):
        counter = 1
        ans = ''
        n = len(s)
        for i, k in enumerate(s):
            if ans is '':
                ans += s[i]
                continue
            
            if s[i] == s[i-1]:
                counter += 1
            if s[i] != s[i-1] or i == n-1:
                if counter > 1:
                    ans += str(counter)
                    counter = 1
                if i != n-1:
                    ans += s[i]
        print(ans)

    def toggle_char(self, s):
        list1 = 'abcdefghijklmnopqrstuvwxyz'
        list2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        for i in s:
            if i in list1:
                temp1 = list1.find(i)
                ans += (list2[temp1])
            elif i in list2:
                temp2 = list2.find(i)
                ans += (list1[temp2])
        print(ans)

    def fac(self, n):
        if n < 2:
            return n
        return self.fac(n-1)+self.fac(n-2)

    def main(self):
        self.substrings("abccbc")
        print(self.palindrome("abaaba"))
        self.string_compression('aaabbccaaaaaaggggdee')
        self.toggle_char('GowTHam')
        self.print_all_permutations("abc")
        

if __name__ == "__main__":
    obj = Solution()
    obj.main()