'''
random
범위를 지정해서 특정 범위의 무작위 수를 뽑는다
'''

import random
'''
for i in range(5):
    print( random.random(), end=" " )
print()

for i in range(5):
    print( random.randrange(0,3), end=" " )


print( "-" * 100 )


#Q1.
print( "#Q1. 로또 프로그램 ")
# 1~45 사이의 무작위 중복되지 않는 6개의 수

s = set()
while len(s) < 6:
    s.add(random.randrange(1,46))
print( s )


ls = list()
while len(ls) < 6:
    num = random.randrange(1, 46)
    if ls.count(num) == 0:
        ls.append(num)
print( ls )


print( "-" * 100 )


#Q2.
print( "#Q2. 업다운 프로그램 ")

rank = 100
while True:
    print( "1. 게임 시작  2. 최고 기록 확인  3. 종료")
    num = int(input(">>> "))
    cnt = 0

    if num == 1:
        com = random.randrange(1, 100)
        print( "com:", com )
        
        while True:
            user = int(input("수 입력: "))
            if com > user:
                print( "up" )
                cnt += 1
            elif com < user:
                print( "down" )
                cnt += 1
            elif com == user:
                print( "정답" )
                cnt += 1
                if cnt < rank:
                    print( "최고 기록 갱신" )
                    rank = cnt
                break
        
    elif num == 2:
        if rank == 100:
            print( "게임 먼저 진행하세요" )
        else:
            print( "최고 기록:", rank )
    elif num == 3:
        print( "종료" )
        break
    else:
        print( "잘못된 입력" )


print( "-" * 100 )
'''

#Q3.
print( "#Q3. 업다운 프로그램 ")

rank = 100
while True:
    print( "1.게임 시작  2.최고 기륵 확인  3. 종료" )
    num = int(input(">>> "))
    ls = []
    cnt = 0

    if num == 1:
        cnt = 0
        com_s = set()

        while True:
            com_s.add(random.randrange(1,10))

            if len(com_s) == 3:
                break
        com = list(com_s)
        print( "com:", com )

        ls = [0, 0, 0]

        while True:
            cnt += 1
            for i in range(3):
                user = int(input("수 입력: "))

                if user == com[i]:
                    ls[0] += 1
                else:
                    ls[2] += 1
            print( f"{ls[0]} 스트라이크, {ls[1]}볼, {ls[2]}아웃" )
            
            if ls[0] == 3:
                break
            ls = [0,0,0]

        if cnt < rank:
            print( cnt,"회. 최고 기록 갱신" )
            rank = cnt
        else:
            print( cnt, "회 만에 맞혔습니다" )

    elif num == 2:
        if rank == 100:
            print( "게임 먼저 진행하세요" )
        else:
            print( "최고 기록:", rank )
    elif num == 3:
        print( "종료" )
        break
    else:
        print( "잘못된 입력" )