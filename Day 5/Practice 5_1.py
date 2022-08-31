# URL을 받아 도메인 추출하기

# 함수 정의

def crolling(url):
    try:
        url_sp = url.split("/")

        web = url_sp[2]
        content = url_sp[3]
        
        if "=" in content:      # 컨텐츠명이 존재하지 않는 주소일 때를 대비
            content = "-"
        elif len(content) <= 2:
            content = "-"
        
        answer = f"SiteName :\t{web}\n ContentName :\t{content}"
        
    except IndexError:        # 컨텐츠명이 존재하지 않아 인덱스 초과 오류가 났을때를 대비
        answer = f"[ {url} ] 은 추출할 수 없습니다. 다시 입력해주세요.\n"
        
    return answer

while 1:

    # URL 받아와서 함수 적용    
    url = input(f" 원하는 URL를 등록해주세요.\n\t: ")
    
    print("\n", crolling(url), "\n")

    # 다시 입력을 원할 경우와 원하지 않을경우    
    new = input(f" 다시하시겠습니까? ( Y / N )\n\t: ")
    
    if new.upper() == "N":
        print("\n 시스템을 종료합니다.\n\n\n 감사합니다.")
        break
    elif new.upper() == "Y":
        print("\n")
        continue
    else:
        # Y나 N 이외의 문자를 입력할 경우
        print("\n 오류로 인해 종료합니다.")
        break
