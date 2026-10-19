import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}

        for s, d, p in flights:
            graph[s].append((d, p))
        
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        heap = [(0, src, 0)]

        while heap:
            cost, node, f = heapq.heappop(heap)
            # Skip outdated
            if cost > dist[node][f]:
                continue
            # Check if reached
            if node == dst:
                return cost
            # Check if already k stops
            if f == k + 1:
                continue
            # Look at neighbors
            for v, p in graph[node]:
                new_cost = cost + p
                if dist[v][f + 1] > new_cost:
                    dist[v][f + 1] = new_cost
                    heapq.heappush(heap, (new_cost, v, f + 1))
        
        return -1

            