# Q4 두가지 수를 입력 받아 최대공약수 출력

a, b = map(int, input("a b\n").split())     # a, b에 두 수를 정수로 저장

lst_a = []                                  # a의 약수
lst_b = []                                  # b의 약수

lst_comb = []                               # a와 b의 공약수

for i in range(1, a+1):                     # a의 약수 뽑기

    if i == 1 | i == a: lst_a.append(i)
    elif a%i == 0: lst_a.append(i)

for i in range(1, b+1):                     # b의 약수 뽑기

    if i == 1 | i == b: lst_b.append(i)
    elif b%i == 0: lst_b.append(i)

for i in lst_a:                             # 공약수 뽑기

    if i in lst_b:

        lst_comb.append(i)

print(f"{a}과(와) {b}의 최대공약수는 {max(lst_comb)} 입니다.")
                                            # 최대공약수 출력
