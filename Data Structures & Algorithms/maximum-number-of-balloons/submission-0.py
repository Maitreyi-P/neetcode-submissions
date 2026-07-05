class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balloon = {
            'b':1,
            'a':1,
            'l':2,
            'o':2,
            'n':1
        }

        string = defaultdict(int)

        for s in text:
            if s in 'balon':
                string[s] += 1

        res = len(text)

        for c in balloon:
            res = min(res, string[c]//balloon[c])

        return res
        

