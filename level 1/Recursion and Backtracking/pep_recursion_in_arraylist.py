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
        if len(s) == 0:
            return [" "]

        ch = s[0]
        res = s[1:]
        res = self.get_kcp(res)

        mres = []
        data = val[int(ch)]
        for i in data:
            for j in res:
                mres.append(i+j)
        return mres

    def get_stair_paths(self, n):
        if n == 0:
            return [" "]
        elif n < 0:
            return []

        paths1 = self.get_stair_paths(n-1)
        paths2 = self.get_stair_paths(n-2)
        paths3 = self.get_stair_paths(n-3)

        path = []

        for i in paths1:
            path.append("1" + i)
        for j in paths2:
            path.append("2" + j)
        for k in paths3:
            path.append("3" + k)

        return path

    def get_maze_path(self, i, j, i1, j1):
        if i > i1 or j > j1:
            return []
        elif i == i1 and j == j1:
            return [" "]

        hor = self.get_maze_path(i, j+1, i1, j1)
        ver = self.get_maze_path(i+1, j, i1, j1)

        path = []
        for a in hor:
            path.append("h"+a)
        for b in ver:
            path.append("v"+b)

        return path

    def get_maze_path_with_jump(self, i, j, i1, j1):
        if i == i1 and j == j1:
            return [" "]

        path = []

        for size in range(1, j1 - j + 1):  # size can be 1, 2, 3 etc.
            hpaths = self.get_maze_path_with_jump(i, j+size, i1, j1)
            for hpath in hpaths:
                path.append("h" + str(size) + hpath)

        for size in range(1, i1 - i + 1):  # size can be 1, 2, 3 etc.
            vpaths = self.get_maze_path_with_jump(i+size, j, i1, j1)
            for vpath in vpaths:
                path.append("v" + str(size) + vpath)

        for size in range(1, i1 - i + 1):  # size can be 1, 2, 3 etc.
            if size <= i1 and size <= j1:
                dpaths = self.get_maze_path_with_jump(i+size, j+size, i1, j1)
                for dpath in dpaths:
                    path.append("d" + str(size) + dpath)

        return path
            

    def main(self):                                                                     
        # print(self.get_subsequence("ab"))
        # print(self.get_kcp("573"))
        # print(self.get_stair_paths(4))
        # print(self.get_maze_path(0, 0, 2, 2))
        print(self.get_maze_path_with_jump(0, 0, 2, 2))


if __name__ == "__main__":
    obj = Solution()
    obj.main()
