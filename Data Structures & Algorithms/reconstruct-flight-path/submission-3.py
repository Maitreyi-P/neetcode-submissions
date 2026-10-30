class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #iterative
        #if aiprort has no dest, add to res. else, add to stack

        tickets.sort(reverse=True)

        adj = defaultdict(list)
        for src,dst in tickets:
            adj[src].append(dst)

        stk = ["JFK"]
        res = []

        while stk:
            curr = stk[-1]

            if not adj[curr]:
                res.append(stk.pop())
            else:
                stk.append(adj[curr].pop())


        return res[::-1]
            
