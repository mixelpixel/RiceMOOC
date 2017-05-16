class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + str(self.y)

    def translate(self, delta_x = 0, delta_y = 0):
        '''Translate the point in the x direction by delta_x
        and in the y direction by delta_y.'''
        self.x += delta_x
        self.y += delta_y
        return self.x, self.y

