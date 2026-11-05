class Solution:
    def simplifyPath(self, path: str) -> str:
        

        stk = []
        curr = ""

        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stk:
                        stk.pop()
                elif curr != "" and curr != ".":
                    stk.append(curr)
                curr = ""
            else:
                curr += c

        res = ""
        for r in stk:
            res +=  "/" + r

        if len(res) == 0:
            return "/"
        return res
