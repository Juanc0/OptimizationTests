class SinglePoint:
    def __init__(self, x, f, children, replace, stop):
        self.x = x
        self.f = f
        self.children = children
        self.replace = replace
        self.stop = stop

    def exe(self):
        iter = 0
        while(not self.stop(iter, self.x, self.f)):
            y = self.children(iter, self.x, self.f)
            self.x = self.replace(iter, self.x, y, self.f)
            iter += 1
        return self.x