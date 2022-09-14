    # font = Casacadia Code

    # sort 실습

s = [14, 12, "book", "1", 94, 0]

print(s.sort())               # str과 int를 섞어서 정렬은 불가



    # read 함수를 통해 읽어와 출력
    
while 1:
    try:
        name = input("\n>\t> [ 파일명.확장자 ] 를 입력해주세요.\n|\t|\n|\t| ")

        file = open(name)      
        txt = file.read().split("\n")
        l = 1

        print("|\t|")

        for i in txt:
            if l < 10:
                print(f"|   {l}   |     {i}")
                l += 1
            else:
                print(f"|  {l}   |    {i}")
                l += 1

        print("|\t|\n>\t>")

        break
    except:
        print("\t|\n|\t| 잘못된 파일명입니다.\n>\t> 다시 입력해주세요.")
        continue


    
    # 텍스트 파일을 읽어온 후 한 라인씩 read

file = open("./test3.txt")    # 텍스트 파일을 읽기전용으로 열기
l = 1
for i in file:
    print(f"{l}    {i}", end = "")
    l += 1
