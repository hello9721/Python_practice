# Class == 객체 == Object

# 객체지향
# 서로 협력하는 여러 개의 객체로 구성
# 각각의 객체가 서로 협력하여 프로그램을 작동시킴

# 분할 정복 ( divide and conquer )
# 문제를 이해가능한 작은 문제로 분할하여 접근

# 클래스 : 형식, 템플릿 => 메소드가 필수
# 메소드 : Class 내의 함수
# 필드 / 속성 : Class 내의 변수
# 객체 / 인스턴스 : 클래스의 인스턴스 == 구체화 == 변수로 선언이 된 클래스

class classname:        # class 클래스명:

    n = 0

    name = ""

    def __init__(self, x): # 생성자
        self.name = x
        print("Hello, there!")
    
    def a(x):           # def 메소드(변수):
        x += 1
        return x
    def d(x):
        x *= 2 
        return x
    def m(self, x):     # self 인수 추가
        x -= self.n     # self.n 아래 설명 참조
        return x
    def self_num(self, x):
        self.n = x

    def __del__(self):  # 소멸자
        print(f"Bye, {self.name}.")

        
                        # self.name = ""
print(classname.a(5))   # classname이라는 클래스의 a() 라는 메소드를 실행
print(classname.d(5))

my_num = classname("hana")
                        # class를 변수에 선언 가능 => 인스턴스로 선언 => 구동
                        # self.name = "hana"

print(my_num.m(5))      # == classname.m(my_num, 5) / self.n == 0 => 0

my_num.self_num(6)      # self.n == 6
print(my_num.m(5))      # => -1

my_num = 8282           # 구동종료 => Bye, hana.

                        # class를 a에 선언하게 되면 메소드를 실행할때
                        # class.method(a) 와 같이 매개변수로 들어가게 된다.
                        # 그것으로 인해 a.method(n) 처럼 사용하고 싶은 변수를 넣었을때
                        # 'method() takes 1 positional argument but 2 were given'
                        # 라는 오류가 뜨게 되고
                        # 이를 막기위해 메소드 선언 시 self 를 같이 매개변수로 넣으면
                        # 제대로 작동한다.

                        # 메소드 안에서 사용되는 self.n 이란,
                        # 클래스 안에서 선언된 n이라는 변수를 말한다.

# init == 생성자
# a = classname() 으로 선언될 때 구동

# del == 소멸자
# a = n 으로 a가 다른 것으로 선언되어 classname()이 더이상 사용되지 않을때 구동종료

