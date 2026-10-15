class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()  # This is on the current path
        visited = set()   # Finished checking

        result = []

        def dfs(course):
            # 1. Currently on DFS path?
            if course in visiting:
                return False  # Cycle!

            # 2. Already fully checked?
            if course in visited:
                return True

            # 3. Add to current path
            visiting.add(course)

            # 4. Explore neighbors
            for nei in graph[course]:
                if not dfs(nei):
                    return False

            # 5. Remove from current path
            visiting.remove(course)

            # 6. Mark as fully checked
            visited.add(course)

            result.append(course)

            return True

        # Builf graph from prerequisites
        graph = {i: [] for i in range(numCourses)}

        for current, prereq in prerequisites:
            graph[current].append(prereq)
        
        flag = True
        for i in range(numCourses):
            if not dfs(i):
                flag = False
        
        if flag:
            return result
        else:
            return []

        



        