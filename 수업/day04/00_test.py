'''
F5 : 디버깅 실행 모드
F9 : 브레이크 포인트
F11 : 한 줄씩 실행
F10 : 한 줄씩 실행
shift + F5 : 디버깅 종료
'''

# sum_ = 0
# for i in range(10000):
#     sum_ += i
# print( sum )


# print( "-" )


# for i in range(5):
#     print( "실행" )
#     for k in range(3):
#         print( "종속" )
#     print( "끝" )


# print( "-" )


# i = 1
# flag = True
# while flag:
#     print( i, "종속 문장", end=" " )
#     if i == 5:
#         flag = False
#     i += 1
# print( "다음 문장 실행" )


'''
break : 반복문을 빠져나올 경우 사용
continue : 반복문 위로 올려보낸다
'''
'''
i = 0
while i <= 5:
    i += 1
    if i == 3:
        break     # i가 3일 때 반복을 멈춤
        print( "333333" )
    print( i, "출력" )
print( "다음 문장" )


print( "-" )


i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue    # i가 3일 때 건너뜀
        print( "333333" )
    print( i, "출력" )
print( "다음 문장" )


print( "-" )


print( " === while else === ")
i = 0
while i < 5:
    i += 1
    print( i, "종속 문장" )
    if i == 2:
        break
else:
    print( "else 실행" )
print( "다음 문장" )


print( "-" * 100 )


#Q1.
print( "#Q1. while과 while else, break와 continue 이용하세요")
# 10 ~ 20 사이의 숫자만 입력받아 1부터 입력받은 수까지의 합을 구하시오

result = 0
i = 1
while True:
    num = int(input("1~10사이의 숫자 입력 : "))
    if num < 10 or num > 20:
        print("잘못 입력 다시")
        continue
    break
while i <= num:
    result += i
    i += 1
else:
    print(f"1 ~ {num}까지의 합 : {result}")


# print( "-" * 100 )


# for i in range(0, 3, 1):
#     for k in range(0, 5, 1):
#         if k == 3:
#             break
#         print( f"i: {i}, k: {k}" )

print( "-" )


i = 0
while i < 3:
    k = 0
    while k < 5:
        if k == 3:
            break
        print( f"i: {i}, k: {k}" )
        k += 1
    i += 1


print( "-" * 100 )


#Q2.
print( "#Q2. 자판기" )
N = int(input("요금을 투입하세요: "))
while True:
    print( "================ 커피 자판기 ================")
    print( "1. 커피(200)  2. 코코아(250)  3. 반환  4. 종료")
    print( f"현재 금액: {N}원" )
    menu = int(input("메뉴를 선택하세요>>> "))
    if menu == 1: 
        if N >= 200:
            print( "맛있게 드세요\n" )
            N = N - 200
            continue
        else:
            print( "요금이 부족합니다\n" )
            continue
        break
    elif menu == 2:
        if N >= 250:
            print( "맛있게 드세요\n" )
            N = N - 250
            continue
        else:
            print( "요금이 부족합니다\n" )
            continue
        break
    elif menu == 3:
        print( f"반환 금액: {N}\n" )
        N = 0
    else:
        print( "종료" )
        break


print( "-" * 100 )


#Q3.
print( "#Q3. 1에서부터 입력된 어떤 수까지 내에 있는 소수를 찾는 프로그램" )
# 1~10 소수: 2,3,5,7

N = int(input("수 입력: "))

for i in range(2, N+1):
    cnt = 0
    for k in range(1, i+1):
        if i % k == 0:
            cnt += 1
    if cnt == 2:
        print( i )
'''


N = int(input("수 입력: "))
print( "1~10까지의 소수: ", end="")

for i in range(1, N+1):
    cnt = 0
    for k in range(1, i+1):
        if i % k == 0:
            cnt += 1
    if cnt == 2:
        print( i, end=", " )
