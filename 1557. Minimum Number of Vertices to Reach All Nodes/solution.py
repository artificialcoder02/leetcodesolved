class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        # Create a set of all nodes
        all_nodes = set(range(n))
        
        # Create a set of destination nodes
        destination_nodes = set(destination for _, destination in edges)
        
        # Compute the set difference between all nodes and destination nodes
        source_nodes = all_nodes - destination_nodes
        
        # Convert the set of source nodes to a list
        return list(source_nodes)
