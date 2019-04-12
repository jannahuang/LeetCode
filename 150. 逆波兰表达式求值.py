# 150. 逆波兰表达式求值
# 20190412

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ls = []
        result = 0
        # 存在 tokens 为 1 的情况，单独处理
        if len(tokens) > 1:
            for i in tokens:
                if i in '+-*/':
                    b = ls.pop()
                    a = ls.pop()
                    # 除法要取整，单独处理
                    if i == '/':
                        # 用 eval 将字符串转为数字计算
                        result = int(eval("{}/{}".format(a,b)))
                    else:
                        result = eval("{}{}{}".format(a, i, b))
                    ls.append(result)
                else:
                    ls.append(i)
            return result
        else:
            return eval(tokens[0])