# 상속 ( Inheritance )
# 부모 클래스를 자식 클래스가 상속 받아 사용

class A:
    
    x = 5                       # Attribute (속성) = Class 내의 변수
    name = ""

    def __init__(self):         # Method (메소드) = Class 내의 함수
        print("hello, there!")
        
    def age_change(self, x):
        self.x = x

    def name_change(self, name):
        self.name = name
        
    def __del__(self):
        print(f"bye, {self.name}, {self.x}")
    
class B(A):                     # A 클래스를 상속 받음.

    def after_n(self, x):
        self.x += x
        return self.x

a = B()

a.age_change(26)                # a는 B만 가져왔지만,
a.name_change("hana")           # B가 A를 상속 받았기에 A의 모든 요소를 사용 가능.

a = "end"

