# 쓰기모드로 열기
# 덮어쓰기 -> 기존 파일의 내용을 다 지운다.
# 지워진 내용은 복구불가

# file = open("C:/Users/user8/Documents/Study/test.txt", 'w')

# file.write("hello")     # hello 라는 텍스트를 써넣기

# file.close()            # 파일을 닫으면 써넣은 문자열은 그대로 저장된채 닫음

# Append 모드로 열기
# 읽는건 안되지만 기존 내용을 불러온 상태에서 바로 이어서 내용 추가는 가능하다.

file = open("C:/Users/user8/Documents/Study/test.txt", 'a')


