class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = [False] * len(isConnected)

        count = 0

        def dfs(i):
            visited[i] = True

            for nei in range(len(isConnected)):
                if isConnected[i][nei] == 1 and not visited[nei]:
                    dfs(nei)

        for i in range(len(isConnected)):
            if not visited[i]:
                count += 1
                dfs(i)

        return count