# Q11 임의의 텍스트 파일에 대해 파일명, 찾을 단어, 바꿀 단어를 입력받아 해당 파일에서 단어를 변환하여 다른 파일로 출력

path = input("경로를 입력해주세요.\n> ")     # 경로
name = input("파일명을 입력해주세요.\n> ")    # 파일명

file = path + "\\" + name               # 전체 경로

f = open(file)                          # 해당 파일 열기

txt = []                                # 파일 내용이 저장될 리스트

for i in f: txt.append(i.split("\n")[0])

f.close()                               # 파일 닫기

print("")

old = input("find : ")                  # 찾을 단어
new = input("replace : ")               # 바꿀 단어

name = name.split(".")                  # 이름과 확장자 분리
file = path + "\\" + name[0] + "_replace." + name[1]
                                        # 저장될 파일의 전체 경로
cnt = 0                                 # 변경 횟수 카운트

f = open(file, "w")                     # 저장될 파일 열기

for i in txt:                           # txt에서 하나씩 빼와서

    if old in i:                        # 찾을 단어가 i 안에 있다면
        
        i = i.replace(old, new)         # i에서 찾아 바꾸어서
        cnt += 1                        # 변경 횟수 + 1

    f.write(f"{i}\n")                   # 파일에 쓰기

f.close()                               # 파일 닫고


print(f"\n저장 경로 > {file}\n\n{cnt}번 변경되었고,\n성공적으로 저장 되었습니다.")
                                        # 저장된 전체경로, 변경횟수 출력
