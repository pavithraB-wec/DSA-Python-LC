class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]

        seen = set()

        for word in words:
            code = []
            for ch in word:
                code.append(morse[ord(ch) - ord('a')])
            seen.add("".join(code))

        return len(seen)