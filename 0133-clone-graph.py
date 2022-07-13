"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}
        if (node == None): return 
        return self.bfs(node, visited)
        
    def bfs(self, original_node, visited):
        if (original_node in visited): 
            return visited[original_node]
        copy = Node(original_node.val)
        visited[original_node] = copy
        for n in original_node.neighbors:
            copy.neighbors.append(self.bfs(n, visited))
        return copy
