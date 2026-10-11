class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Put words into Trie
        root = TrieNode()
        for word in words:
            node = root
            for w in word:
                if w not in node.children:
                    # New word start
                    node.children[w] = TrieNode()
                # If already noted there, just move on
                node = node.children[w]

            node.word = word

        res = []
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, node):

            # 1. Out of range
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            char = board[r][c]

            # 2. Used
            if char == "#":
                return

            # 3. Not in Trie
            if char not in node.children:
                return

            # 4. Proceed in Trie
            node = node.children[char]

            # 5. find the word
            if node.word is not None:
                res.append(node.word)
                node.word = None

            # 6. mark visited
            board[r][c] = "#"

            # 7. other directions continue
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # 8. backtrack
            board[r][c] = char
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res


        