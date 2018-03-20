class Bit(object):
    def __init__(self, l):
        if isinstance(l, int):
            self.ar = [0 for _ in range(l+1)]
        else:
            self.ar = [0] + l

    def __getitem__(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.ar[i]
            i = i & (i - 1)
        return res

    def update(self, i, val):
        i += 1
        while i < len(self.ar):
            self.ar[i] += val
            i = i + (i & (-i))

