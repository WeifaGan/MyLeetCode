class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int: 
        index1, index2 = float('inf'), float('-inf')
        min_p = len(words)
        for index, word in enumerate(words):
            if word == word1:
                index1 = index
            elif word == word2:
                index2 = index
            min_p = min(min_p,abs(index1-index2))
        return min_p
