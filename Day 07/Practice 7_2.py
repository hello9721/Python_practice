    # 파일 안의 텍스트는 총 몇줄?

file = open("./BOJ/chess problem.py")

count = 0
for i in file:
    count += 1
    
print(f"Total Lines = {count}")

    # file.read() 은 텍스트 파일 하나를 하나의 문자열로 읽어준다.
    # ./ 현재 폴더를 가리키는 상대적인 경로
    # ../ 현재 폴더의 부모 폴더를 가리키는 상대적인 경로

str_file = open("../test.txt").read()
print(f"\n{str_file}\n")
