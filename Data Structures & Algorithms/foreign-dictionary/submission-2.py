# create a directed graph of all unique letters and "." as verticies :
# suppose . < all letters
# so add edges from . to all letters
# loop letter_position<= longest word:
#   loop i<j: 
#       if the letters differ then add edge (word[i][letter_position], word[j][letter_position])
# return any topological sorting starting from ".".   but if there is a cycle then return ""
# to handel strings of different sizes you can suppose they are padded "."
# example :
# ["abc","ab"] should be considered as: ["abc","ab."] i.e. word[j][letter_position].get's default val is "." 
# actually to save time if it is about to add an edge from any letter to "." then there will be a cycle and return "" but of course there is more complicated hiden cycle to detect later
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Find longest word length
        longest_len = max(len(word) for word in words)
        
        # Pad all words with "." to same length
        padded_words = [word + "." * (longest_len - len(word)) for word in words]
        
        # Build graph with "." as start node
        graph = {"." : set()}
        in_degree = {".": 0}
        
        # Initialize all letters
        for word in padded_words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
                    in_degree[char] = 0
        
        # Add edges from "." to all letters
        for word in padded_words:
            for char in word:
                if char != ".":
                    if char not in graph["."]:
                        graph["."].add(char)
                        in_degree[char] += 1
        
        # Loop through positions and compare letters
        for i in range(len(padded_words) - 1):
            for j in range(i + 1, len(padded_words)):
                edited = False 
                for pos in range(longest_len):
                    char_i = padded_words[i][pos]
                    char_j = padded_words[j][pos]
                    print(i, char_i, j, char_j)
                    
                    # If letters differ, add edge
                    if char_i != char_j and char_i != ".":
                        if char_j not in graph[char_i]:
                            graph[char_i].add(char_j)
                            in_degree[char_j] += 1
                        edited = True
                        break
                if edited:
                    break
        # Topological sort starting from "."
        queue = ["."]
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for neighbor in sorted(graph[node]):  # sorted for consistent order
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        print(graph)
        print(result)
        # If cycle exists, return ""
        if len(result) != len(graph):
            return ""
        
        # Remove "." from result
        return "".join(result[1:])