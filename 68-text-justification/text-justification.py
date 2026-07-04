class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        i = 0

        while i < len(words):
            line_length = len(words[i])
            j = i + 1

            # Pack as many words as possible
            while j < len(words) and line_length + 1 + len(words[j]) <= maxWidth:
                line_length += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(word) for word in line_words)
            spaces = maxWidth - total_chars

            # Last line or single word -> Left justify
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                gaps = num_words - 1
                even_spaces = spaces // gaps
                extra_spaces = spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (even_spaces + (1 if k < extra_spaces else 0))

                line += line_words[-1]

            result.append(line)
            i = j

        return result