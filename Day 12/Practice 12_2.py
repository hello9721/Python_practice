# from 같은 디렉토리의 다른 파일 import 사용할 클래스 as 사용할 이름

from Practice_12_1 import point as p

# 해당 파일에서 import 해온 클래스의 메소드를 전부 사용 가능

a = p(5, 5)
b = p(5, 6)

ab1 = a + b
ab2 = a - b
ab3 = a * 80
ab4 = a * b

print(ab1.x, ab1.y)
print(ab2.x, ab2.y)
print(ab3.x, ab3.y)
print(ab4.x, ab4.y)
