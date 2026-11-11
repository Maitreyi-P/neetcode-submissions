class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parent[rootx] = rooty


        N = len(accounts)
        parent = [i for i in range(N)]

        emailmap = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in emailmap:
                    emailmap[email] = i
                else:
                    union(i,emailmap[email])


        groups = defaultdict(list)
        for email, idx in emailmap.items():
            root = find(idx)
            groups[root].append(email)

        res = []
        for idx, emails in groups.items():
            res.append([accounts[idx][0]] + sorted(emails))
            

        return res
