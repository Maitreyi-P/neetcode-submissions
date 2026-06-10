class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p,s in zip(position,speed)]

        stk = []
        for p,s in sorted(pairs)[::-1]:
           time = (target-p)/s
           stk.append(time)
           if len(stk) >= 2 and stk[-1] <= stk[-2]:
            stk.pop()

        return len(stk)


#check the time taken by each car and add to stack, if time of t.o.s is lesser that previous top, pop the top

