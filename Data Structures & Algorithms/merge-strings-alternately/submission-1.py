class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shortest = min(len(word1), len(word2))
        i=0
        len1 = len(word1)
        len2 = len(word2)
        combined=[]

        while i<shortest:
            combined.append(word1[i])
            combined.append(word2[i])
            i+=1
        
        full_word = ''.join(combined)
        return full_word + word1[shortest:] + word2[shortest:]



        