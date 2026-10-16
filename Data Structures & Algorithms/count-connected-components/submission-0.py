class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Builf graph from prerequisites
        graph = {i: [] for i in range(n)}

        for current, prereq in edges:
            graph[current].append(prereq)
            graph[prereq].append(current)
        
        visited = set()
        count = 0

        def dfs(node):
            # Mark node as visited
            visited.add(node)
            # Explore unvisited neighbors
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        # Check every node
        for i in range(n):
            if i not in visited:
                # If unvisited
                count += 1
                dfs(i)
   

        return count
        