class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.ds = []
        for k in vec2d:
            for j in k:
                self.ds.append(j)
        print self.ds
        self.i = 0

    def next(self):
        """
        :rtype: int
        """
        res =  self.ds[self.i]
        self.i += 1
        return res
        
    def hasNext(self):
        """
        :rtype: bool
        """
        # print not self.i == len(self.ds) - 1
        return not self.i == len(self.ds)


if __name__ == '__main__':
    i, v = Vector2D([[1,2],[],[5,6]]), []
    while i.hasNext():
        v.append(i.next())   
    print v