class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}

        # 1. Compare adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
        #    - Check invalid prefix
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
        #    - Find first differing character
            j = 0
            char1 = None
            char2 = None
            while j < len(word1) and j < len(word2):
                if word1[j] != word2[j]:
                    char1 = word1[j]
                    char2 = word2[j]
                    break
                else:
                    j += 1
        
        #    - Add directed edge
            if char1:
                graph[char1].add(char2)

        visiting = set()
        visited = set()
        result = []

        def dfs(c):
            # 2. Detect cycle
            if c in visiting:
                return False
            
            if c in visited:
                return True
            
            visiting.add(c)

            # 3. Explore neighbors
            for nn in graph[c]:
                if not dfs(nn):
                    return False

            # 4. Postorder append
            visiting.remove(c)
            visited.add(c)
            result.append(c)
            return True

        # 5. DFS all characters
        for key, value in graph.items():
            if not dfs(key):
                return ""

        # 6. Reverse result and join into string
        result.reverse()
        return "".join(result)