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

    def main(self):
        # self.substrings("abccbc")
        # print(self.palindrome("abaaba"))
        # self.string_compression('aaabbccaaaaaaggggdee')


if __name__ == "__main__":
    obj = Solution()
    obj.main()
