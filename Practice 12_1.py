# operator override
# 수치 연산자 메소드

# point == 2D point

# P1 + P2 를 했을 때 P3(x1+x2, y1+y2) 가 생성되도록

class point:

    x = 0
    y = 0

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, P):

        x = self.x + P.x
        y = self.y + P.y
        
        P3 = point(x, y)

        return P3

P1 = point(3, 6)
P2 = point(7, 2)

P3 = P1 + P2

print(P3.x, P3.y)
