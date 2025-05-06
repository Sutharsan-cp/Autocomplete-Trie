class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0  # To track word frequency

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.frequency += 1  # Increment frequency for this word

    def _collect_words(self, node, prefix, words):
        if node.is_end:
            words.append((prefix, node.frequency))
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)

    def autocomplete(self, prefix, limit=5):
        node = self.root
        prefix = prefix.lower()
        # Traverse to the prefix node
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        # Collect all words starting from this node
        words = []
        self._collect_words(node, prefix, words)
        # Sort by frequency (descending) and then alphabetically
        words.sort(key=lambda x: (-x[1], x[0]))
        # Return top 'limit' suggestions
        return [word for word, freq in words[:limit]]

# Load words from a file into the Trie
def load_dictionary(trie, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                if word:
                    trie.insert(word)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")