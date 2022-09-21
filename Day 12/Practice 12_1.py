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

    def __mul__(self, M):       # 다형성
                                # 같은 이름을 가진 함수가 있을 때
        x = self.x * M          # 그 뒤에 붙는 인수에 따라 적용 함수가 달라진다.
        y = self.y * M

        return point(x, y)

    def __mul__(self, P):

        x = self.x * P.x
        y = self.y * P.y

        return point(x, y)


P1 = point( 0, 7 )
P2 = point( 1, 5 )

P3 = P1 + P2
P4 = P1 - P2            # __sub__
P5 = P2 * 200           # Scalar 곱셈
P6 = P1 * P2            # Vector 곱셈


print( P3.x, P3.y )
print( P4.x, P4.y )
print( P5.x, P5.y )
print( P6.x, P6.y )
