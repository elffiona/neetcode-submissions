class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue

                if nei in visited:
                    return False  # Cycle!

                if not dfs(nei, node):
                    return False

            return True
        
        # Builf graph from prerequisites
        graph = {i: [] for i in range(n)}

        for current, prereq in edges:
            graph[current].append(prereq)
            graph[prereq].append(current)

        if not dfs(0, -1):
            return False

        return len(visited) == n