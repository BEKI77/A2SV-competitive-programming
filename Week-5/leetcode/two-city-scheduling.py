class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key = lambda x: x[0]-x[1])
        ans = 0
        for i in range(0,n//2):
            ans+=costs[i][0]
        for i in range(n//2,n):
            ans+=costs[i][1]
        return ans