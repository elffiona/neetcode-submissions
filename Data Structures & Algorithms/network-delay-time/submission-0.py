import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build directed weighted graph
        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        # 2. Initialize distances
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # 3. Initialize min heap
        heap = [(0, k)]

        # 4. Dijkstra
        while heap:
            distance, u = heapq.heappop(heap)

            # Skip outdated entries
            if distance > dist[u]:
                continue

            for v, weight in graph[u]:
                # Calculate new distance
                new_dist = dist[u] + weight

                # If shorter, update dist[v]
                # and push (new_distance, v)
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        # 5. Return network delay
        answer = max(dist[1:])
        return answer if answer != float('inf') else -1
        