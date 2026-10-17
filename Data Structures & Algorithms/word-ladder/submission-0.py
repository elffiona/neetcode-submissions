from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        q = deque([(beginWord, 1)])

        while q:
            word, distance = q.popleft()

            # Check if match end word
            if word == endWord:
                return distance
            
            # All neighbors
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i+1:]

                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word, distance + 1))

        return 0
