class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        parent = [i for i in range(n)]

        
        def find(i):

            if parent[i] != i:
                parent[i] = find(parent[i])
            
            return parent[i]

        res = n

        for u, v in edges:

            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                parent[root_u] = root_v
                res -= 1
        
        return res
