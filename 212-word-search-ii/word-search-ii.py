class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = None


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Build Trie
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node.children:
                return

            nxt = node.children[ch]

            # Found a word
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None   # Avoid duplicates

            board[r][c] = "#"

            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "#"):
                    dfs(nr, nc, nxt)

            board[r][c] = ch

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return result