# 150. �沨�����ʽ��ֵ
# 20190412

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ls = []
        result = 0
        # ���� tokens Ϊ 1 ���������������
        if len(tokens) > 1:
            for i in tokens:
                if i in '+-*/':
                    b = ls.pop()
                    a = ls.pop()
                    # ����Ҫȡ������������
                    if i == '/':
                        # �� eval ���ַ���תΪ���ּ���
                        result = int(eval("{}/{}".format(a,b)))
                    else:
                        result = eval("{}{}{}".format(a, i, b))
                    ls.append(result)
                else:
                    ls.append(i)
            return result
        else:
            return eval(tokens[0])