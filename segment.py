def next_power_of_two(n):
    ans = 1
    while ans < n:
        ans *= 2
    return ans

class SegmentTree(object):
    def __init__(self, arr, merge=lambda x,y: x+y, default_val=0):
        self.merge = merge
        self.arr = arr
        self.n = len(arr)
        self.default_val = default_val
        self.tree = [self.default_val] * (2 * next_power_of_two(self.n) - 1)
        self.initialize(0, self.n-1, 0)

    def initialize(self, start, end, index):
        if start == end:
            self.tree[index] = self.arr[start]
            return self.tree[index]

        mid = (start + end) // 2
        a = self.initialize(start, mid, index * 2 + 1)
        b = self.initialize(mid+1, end, index * 2 + 2)
        self.tree[index] = self.merge(a, b)
        return self.tree[index]

    def get_range(self, start, end):
        return self._get_range(0, self.n-1, start, end, 0)

    def _get_range(self, sstart, send, start, end, index):
        if start <= sstart and send <= end:
            return self.tree[index]
        if sstart > end or send < start:
            return self.default_val
        mid = (sstart + send) // 2
        return self.merge(self._get_range(sstart, mid, start, end, 2*index+1),
                self._get_range(mid+1, send, start, end, 2*index+2))

    def update(self, index, diff):
        self.arr[index] = self.merge(self.arr[index], diff)
        self._update(0, self.n-1, index, diff, 0)

    def _update(self, start, end, index, diff, sindex):
        if index < start or index > end: return
        self.tree[sindex] = self.merge(self.tree[sindex], diff)

        if start != end:
            mid = (start + end) // 2
            self._update(start, mid, index, diff, sindex*2+1)
            self._update(mid+1, end, index, diff, sindex*2+2)

    def replace(self, index, newval):
        self.arr[index] = newval
        self._replace(0, self.n-1, index, newval, 0)

    def _replace(self, start, end, index, newval, sindex):
        if index < start or index > end: return

        if start != end:
            mid = (start + end) // 2
            self._replace(start, mid, index, newval, sindex*2+1)
            self._replace(mid+1, end, index, newval, sindex*2+2)
            self.tree[sindex] = self.merge(self.tree[sindex*2+1], self.tree[sindex*2+2])
        else:
            self.tree[sindex] = newval

    def __getitem__(self, index):
        return self.arr[index]


if __name__ == '__main__':
    from random import randint
    n = 10 ** 5
    a = [i for i in range(n)]
    s = SegmentTree(a)

    for _ in range(10**5):
        l = randint(0, n-1)
        r = randint(l, n-1)
        assert s.get_range(l, r) == (l + r) * (r - l + 1) // 2
