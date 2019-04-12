# 20. ÓÐÐ§µÄÀ¨ºÅ
# 20190409

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in match:
                if stack:
                    top = stack.pop()
                else:
                    top = ""
                if match[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack
