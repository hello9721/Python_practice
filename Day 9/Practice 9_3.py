    # mode = "rb" => binary 모드로 열기
    # b'~~~\r\n'

file = open("test3.txt", mode = "rb")

for i in file:
    print(f"\t{i}")

