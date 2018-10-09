class Graph(object):
    def __init__(self, n, undirected=True):
        self.adj = [[] for _ in range(n+1)]
        self.undirected = undirected

    def __getitem__(self, i):
        return self.adj[i]

    def add_edge(self, a, b):
        self.adj[a].append(b)
        if self.undirected:
            self.adj[b].append(a)

    def get_tree(self, root):
        assert root < len(self.adj)
        q = [root]
        parent = {root: None}
        while q:
            node = q.pop(0)
            for child in self.adj[node]:
                if child not in parent:
                    parent[child] = node
                    q.append(child)
        return parent

