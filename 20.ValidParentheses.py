from collections import deque

class Solution: #スタック
    def isValid(self, s: str) -> bool:
        pairs = [{"(",")"},{"[","]"},{"{","}"}]
        d = deque()
        for c in s:
            # print(c)
            # print(d)
            if d == deque():
                d.append(c)
                # print(d)
                continue
            c_stack = d.pop()
            test_set = set([c,c_stack])
            # print(test_set)
            if test_set in pairs:
                # print("a")
                continue
            else:
                d.append(c_stack)
                d.append(c)
        if d == deque():
            print("true")
            return True
        else:
            print("false")
            return False
