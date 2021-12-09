class Solution:

    def get_subsequence(self, s):
        if len(s) == 0:
            return [" "]

        ch = s[0]
        res = s[1:]
        res = self.get_subsequence(res)

        mres = []
        for i in res:
            mres.append(i)
            mres.append(ch+i)
        return mres

    def get_kcp(self, s):
        val = {0: ".;", 1: "abc", 2: "def", 3: "ghi", 4: "jkl", 5: "mno", 6: "pqrs", 7: "tu", 8: "vwx", 9: "yz"}
        if len(s) == 0: #1
            return [" "]

        ch = s[0] #2
        res = s[1:] #3
        res = self.get_kcp(res) #4

        mres = []
        data = val[int(ch)] #5
        for i in data: #6
            for j in res:
                mres.append(i+j)
        return mres



    def main(self):                                                                     
        # print(self.get_subsequence("ab"))
        print(self.get_kcp("573"))



if __name__ == "__main__":
    obj = Solution()
    obj.main()
