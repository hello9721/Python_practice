while 1:
    try:
        t = input()

        if t.upper() == "END" or t.upper() == "E":
            print("\n종료하겠습니다.\n")
            
            break
        else:
            if "." in t:
                a, b = map(int, t.split("."))
                if b != 0:
                    print(f"\n실수 입니다.\n\t=====> {t}\n")
                    print("종료하시려면 END 혹은 E 를 입력해주세요.\n")
                else:
                    print(f"\n정수 입니다.\n\t=====> {t}\n")
                    print("종료하시려면 END 혹은 E 를 입력해주세요.\n")
            else:
                t = int(t)
                print(f"\n정수 입니다.\n\t=====> {t}\n")
                print("종료하시려면 END 혹은 E 를 입력해주세요.\n")
            
    except:
        print("\n숫자만 입력해주세요.\n")
        print("종료하시려면 END 혹은 E 를 입력해주세요.\n")
        
        continue
