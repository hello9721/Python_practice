# __sub__

class point:

    x = 0
    y = 0

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __sub__(self, P):

        x = self.x - P.x
        y = self.y - P.y

        return point(x, y)

P1 = point( 0, 7 )
P2 = point( 1, 5 )

P3 = P1 - P2

print( P3.x, P3.y )
