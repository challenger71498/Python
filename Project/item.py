import grid


class Item:
    name = ""
    price = 0
    weight = 0

    sizeW = 0
    sizeH = 0
    orientation = [0, 0]
    gridMatrix = list()

    def __init__(self, n, p, wei, w, h, x, y):
        self.name = n
        self.price = p
        self.weight = wei

        self.sizeW = w
        self.sizeH = h
        self.orientation = [x, y]
        self.generate_matrix()

    def generate_matrix(self):
        for i in range(self.sizeH):
            self.gridMatrix.append(list())
            for j in range(self.sizeW):
                self.gridMatrix[i].append(grid.Grid())

    def enable_up(self):
        for Grid in self.gridMatrix[0]:
            Grid.up = 1

    def enable_down(self):
        for Grid in self.gridMatrix[-1]:
            Grid.down = 1

    def enable_left(self):
        for i in range(self.sizeH):
            self.gridMatrix[i][0].left = 1

    def enable_right(self):
        for i in range(self.sizeH):
            self.gridMatrix[i][-1].right = 1

