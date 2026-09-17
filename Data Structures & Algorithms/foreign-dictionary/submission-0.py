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
        # Build graph of letter ordering relationships
        graph = {char: [] for word in words for char in word}
        in_degree = {char: 0 for word in words for char in word}
        
        # Extract ordering constraints by comparing consecutive words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # word1[j] comes before word2[j]
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].append(word2[j])
                        in_degree[word2[j]] += 1
                    break
            else:
                # If no difference found and word1 is longer, impossible order
                if len(word1) > len(word2):
                    return ""
        
        # Topological sort using BFS (Kahn's algorithm)
        queue = [char for char in graph if in_degree[char] == 0]
        result = []
        
        while queue:
            char = queue.pop(0)
            result.append(char)
            
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we didn't visit all characters, there's a cycle
        return "".join(result) if len(result) == len(graph) else ""