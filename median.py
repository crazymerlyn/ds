from heapq import *

class Median(object):
    def __init__(self, arr):
        self.small = []
        self.big = []
        for x in arr: self.add(x)

    def add(self, el):
        if len(self.small) == len(self.big):
            heappush(self.small, -el)
        else:
            heappush(self.big, el)

    def median(self):
        if len(self.small) == len(self.big):
            return (self.big[0] - self.small[0]) / 2.
        else:
            return -self.small[0]
