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
