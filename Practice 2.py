try:
    x = int(input("x : "))
    

    if x < 2 :
        print("Below 2")
    elif x == 2 :
        print("Two")
    else :
        print("Something else")




    if x < 2 :
        print("Below 2")
    elif x < 10 :
        print("Below 10")
    elif x < 20 :
        print("Below 20")
    else :
        print("Something else")

except:
    print("숫자만 입력해주세요.")
