class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matches = []
        for word in sorted(words, key=len):
            for w in words : 
                if word in w and word != w: 
                    matches.append(word)
                    break
        return matches

        