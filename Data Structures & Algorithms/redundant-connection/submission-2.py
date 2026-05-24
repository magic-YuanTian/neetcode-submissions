class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        parent = [i for i in range(n+1)]

        def find(i):

            if parent[i] != i:
                parent[i] = find(parent[i])

            return parent[i]

        
        for u, v in edges:
            u_root = find(u)
            v_root = find(v)

            if u_root == v_root:
                return [u, v]
            
            parent[u_root] = v_root
        
        return []
        