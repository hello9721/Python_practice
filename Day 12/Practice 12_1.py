# operator override
# 수치 연산자 메소드

# point == 2D point

# __add__
# __sub__
# __mul__

class point:

    x = 0
    y = 0

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, P):

        x = self.x + P.x
        y = self.y + P.y
        
        return point(x, y)

    def __sub__(self, P):

        x = self.x - P.x
        y = self.y - P.y

        return point(x, y)

    def __mul__(self, M):

        if ( type(M) == point ) :   # M이 point 클래스라면

            x = self.x * M.x        # Vector 곱셈
            y = self.y * M.y

        else:                       # 아니라면
            
            x = self.x * M          # Scalar 곱셈
            y = self.y * M
            
        return point(x, y)


P1 = point( 10, 7 )
P2 = point( 5, 6 )

P3 = P1 + P2            # __add__
P4 = P1 - P2            # __sub__
P5 = P2 * 200           # Scalar 곱셈
P6 = P1 * P2            # Vector 곱셈


print( P3.x, P3.y )
print( P4.x, P4.y )
print( P5.x, P5.y )
print( P6.x, P6.y )


