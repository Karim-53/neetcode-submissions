class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie from words
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['.'] = word  # Mark end of word
        
        result = set()
        visited = set()
        
        def dfs(i, j, node):
            # Base cases
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if (i, j) in visited:
                return
            
            char = board[i][j]
            if char not in node:  # Prune: char not in trie path
                return
            
            # Explore this path
            visited.add((i, j))
            next_node = node[char]
            
            # Check if we found a complete word
            if '.' in next_node:
                result.add(next_node['.'])
            
            # Continue DFS in 4 directions
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + di, j + dj, next_node)
            
            visited.remove((i, j))  # Backtrack
        
        # Start DFS from each cell
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie)
        
        return list(result)