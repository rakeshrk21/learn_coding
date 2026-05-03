class Solution:
    def isValid(self, s: str) -> bool :
        dict = {}
        dict["{"] = "}"
        dict["("] = ")"
        dict["["] = "]"
        stack = []
        
        for c in s:
            if c in dict:
                stack.append(c)
            else:
                if not stack:
                    return False
                if dict[stack.pop()] != c:
                    return False
        
        # if stack:
        #     return False
        # else:
        #     return True

        return not stack


if __name__ == "__main__":
     print(Solution().isValid("({})"))
