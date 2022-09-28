# Q10 입력받은 선택에 따라 다른 기능을 수행하는 프로그램 작성 ( 기능은 3가지 이상 )


def is_p(lst):
            
    return lst == lst[ : : -1]



while 1:
    select = input("모드를 선택하세요.:\n\n1) 회문\n2) 최대공약수\n3) 피라미드\n4) 구구단표\n그외의 입력) 종료\n\n> ")

    print("\n")
    
    if select == "1":

        str = input("단어를 입력해주세요.\n단어에 포함된 가장 긴 회문을 알려드릴게요.\n> ")    
        lst = []
        p_lst = []

        for i in range(len(str)):

            for j in range(i+2, len(str)+1):
                                 
                if is_p(str[i:j]):

                    lst.append(len(str[i:j]))                                                                  
                    p_lst.append(str[i:j])

        print("\n")
                                        
        try: print(f'가장 긴 회문은 " {max(lst)} " 자의 " {p_lst[lst.index(max(lst))]} " 입니다!')
        except: print("회문이 없습니다.")

        print("\n")

    elif select == "2":

        a, b = map(int, input("두 수 a와 b를 입력하세요.\n> ").split())     

        lst_a = []                                  
        lst_b = []                                  

        lst_comb = []                               

        for i in range(1, a+1):                     

            if i == 1 | i == a: lst_a.append(i)
            elif a%i == 0: lst_a.append(i)

        for i in range(1, b+1):                     

            if i == 1 | i == b: lst_b.append(i)
            elif b%i == 0: lst_b.append(i)

        for i in lst_a:                             

            if i in lst_b:

                lst_comb.append(i)

        print(f"{a}과(와) {b}의 최대공약수는 {max(lst_comb)} 입니다.")

        print("\n")

    elif select == "3":
        
        n = int(input("홀수를 입력하세요.\n> "))
        symbol = input("어떤 걸로 쌓을까요? 1 글자 이상 입력시 피라미드가 삐뚤어집니다.\n> ")
        
        b = int(n/2) + 1
        
        cnt = 0                             

        for i in range(1, n+1):             
            if i%2 == 1:                    
                cnt += 1                    
                print(" "*(b-cnt), f"{symbol*i}", sep="")

        print("\n")

    elif select == "4":

        n = int(input("몇 단을 출력할까요? 0 을 입력하면 모두 출력됩니다.\n> "))

        if n == 0:

            for i in range(2, 10):

                for j in range(1, 10):

                    print(f"{i} * {j} = {i*j}")

                print("")
        else:

            for i in range(1, 10):

                print(f"{n} * {i} = {n*i}")
        
        print("\n")

        
    else:
        break
