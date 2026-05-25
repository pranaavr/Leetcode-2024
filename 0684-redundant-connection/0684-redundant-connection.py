class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # 0 to n (inclusive), although 0 isn't included

        # parent is itself at start (parents[3] = 3)
        parent = [i for i in range(len(edges)+1)]
        # rank is 1 since only one node in set at start
        rank = [1 for _ in range(len(edges)+1)]

        # find set representative
        def find(node):
            if node == parent[node]:
                return node
            node = parent[node]
            return find(node)

        for u, v in edges:
            urep = find(u)
            vrep = find(v)
            if urep == vrep:
                return [u, v]
            if rank[urep] >= rank[vrep]:
                rank[urep] += rank[vrep]
                parent[vrep] = urep
            else:
                rank[vrep] += rank[urep]
                parent[urep] = vrep
