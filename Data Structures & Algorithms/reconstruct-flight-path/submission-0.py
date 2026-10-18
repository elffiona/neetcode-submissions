class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        result = []

        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse=True)
                
        def dfs(airport):
            if airport in graph:
                while graph[airport]:
                    n_airport = graph[airport].pop()
                    dfs(n_airport)
                result.append(airport)
            else:
                result.append(airport)
        
        dfs("JFK")

        # reverse
        result.reverse()

        return result