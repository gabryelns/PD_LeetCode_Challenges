class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # pre-calculate string lengths
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        min_distance = [[float("inf")] * (len_word2 + 1) for _ in range(len_word1 + 1)]

        for i in range(len_word1 + 1):
            min_distance[i][len_word2] = len_word1 - i
            
        for j in range(len_word2 + 1):
            min_distance[len_word1][j] = len_word2 - j
            
        for i in range(len_word1 - 1, -1, -1):
            for j in range(len_word2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    min_distance[i][j] = min_distance[i+1][j+1]
                else:
                    min_distance[i][j] = 1 + min(
                        min_distance[i+1][j+1],
                        min_distance[i+1][j],
                        min_distance[i][j+1]
                    )
        
        return min_distance[0][0]
          
print(Solution.minDistance(Solution, "horse", "ros"))
        