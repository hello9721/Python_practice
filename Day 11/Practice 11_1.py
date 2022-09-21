# class -> 변수(속성) / 함수(메소드)
# 인스턴스가 생성될 때마다 클래스 내 변수가 생성
# 함수는 미리 생성되어있다가 사용
# in Python 모든 데이터 / 함수 ==  객체

# 보통 __init__은 받아온 값을 통해 class 내부 속성의 값을 초기화 시켜주는 일을 한다.

# self
# 객체를 호출한 자신이 생성자와 함수에 자동을 전달되도록 하는 역할
# 관례적으로 self를 쓰긴하지만 다른 이름을 사용해도 상관 없음

# class -> 객체를 만들기 위한 틀
# 변수 -> 객체를 구성하는 데이터
# 메소드 -> 변수에 대해 기능을 수행하는 함수
# 생성자, 소멸자 -> 객체 생성과 소멸 시에 자동 호출


# 클래스 안쪽에 'pass' 사용 가능
# 나머지는 그냥 통과한다는 뜻


# operator override
# 수치 연산자 메소드

# +

def __add__(self, other)

# -

def __sub__(self, other)

# *

def __mul__(self, other)

# /

def __truediv__(self, other)

# //

def __floordiv__(self, other)

# %

def __mod__(self, other)

# **

def __pow__(self, other[, modulo])

# >

def __gt__(self, other)

# >=

def __ge__(self, other)

# <

def __lt__(self, other)

# <=

def __le__(self, other)

# ==

def __eq__(self, other)

# !=

def __ne__(self, other)
