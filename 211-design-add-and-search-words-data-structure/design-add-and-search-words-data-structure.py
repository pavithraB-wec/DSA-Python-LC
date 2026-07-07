class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(node, index):
            if index == len(word):
                return node.isEnd

            ch = word[index]

            if ch == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            if ch not in node.children:
                return False

            return dfs(node.children[ch], index + 1)

        return dfs(self.root, 0)