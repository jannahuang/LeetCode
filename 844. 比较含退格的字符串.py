# 844. 比较含退格的字符串
# 20190411

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def result(L):
            ls = []
            for i in L:
                if i == '#' and ls:
                    ls.pop()
                elif i == '#':
                    continue
                else:
                    ls.append(i)
            return "".join(ls)
            
        return result(S) == result(T)
