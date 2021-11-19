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


if __name__ == '__main__':
    obj = Basics()
    obj.Z(5)