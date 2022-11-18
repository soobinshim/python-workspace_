
# ls = []
# #ls = list()
# for i in range(3):
#     value = input(f"{i}.번째 입력: ")
#     ls.append(value)    # 리스트에 데이터 추가
# print( f"총 개수: {len(ls)}" )
# print( f"type: {type(ls)}" )
# print( f"ls: {ls}" )

# ls = []
# print( f"초기화 후 ls: {ls}" )


# print( "-" )


# ls = [30, 10, 20, 40]
# print( "ls: ", ls )
# ls.pop()        # 가장 마지막 값 제외
# print( "pop: ", ls )
# ls.reverse()    # 데이터 뒤집어 줌
# print( "reverse: ", ls )
# ls.sort()       # 오름차순 정렬
# print( "sort: ", ls )


# print( "-" * 100 )


# #Q1.
# print( "#Q1." )
# # ls = [10, 50, 70, 30, 20]
# # arr: ls가 가지고 있는 값을 역으로 저장
# # sort_arr : 오름차순으로 저장
# # reverse_arr : 내림차순으로 저장

# ls = [10, 50, 70, 30, 20]
# arr = ls.copy()
# print( ls )
# arr.reverse()
# print( arr )

# sort_arr = ls.copy()
# sort_arr.sort()
# print( sort_arr )

# reverse_arr = ls.copy()
# reverse_arr.sort()
# reverse_arr.reverse()
# print( reverse_arr )


# print( "-" * 100 )


# ls = [10,20,30]
# print( "ls: ", ls )
# del( ls[1] )    # del 값을 삭제해 주는 파이썬 기능
# print( "del(ls.1): ", ls )

# ls.remove(30)   # ls가 가지고 있는 값을 넣어 삭제
# print( "remove(30): ", ls)


# print( "-" )


# ls = [30,20,10]
# print( ls )
# i = ls.index(20)    # ls가 가지고 있는 값의 위치를 알려 줌
# print( "index(20): ", i )

# ls.append(100)
# print( "append(100): ", ls )

# ls.insert(2,500)    # [2] 위치에 500값을 넣어 주라. 특정 위치에 값 넣기
# print( "insert(2,50): ", ls )

# arr = [1,2,3,1]
# #ls = ls + arr
# ls.extend( arr )    # 값을 합쳐 준다
# print( ls )

# cnt = ls.count("없")   # 1이라는 값이 몇 개 있는지? 값이 있는지 없는지 알 수 있음
# print( "count(1): ", cnt )


# print( "-" * 100)


#Q2.
print( "#Q2. 프로그램 만들기 (단톡방 참조)" )
ls = []
while True:
    print( "===============================================================================" )
    print( "1. 이름 저장  2. 모든 이름 출력  3. 특정 이름 삭제  4. 특정 이름 수정  5. 종료" )
    print( "===============================================================================" )
    N = int(input("입력>>> "))
    
    if N == 1:
        name = input("이름: ")
        if N != name:
            ls.append(name)
            print( "저장됐습니다" )
        else:
            print( "이미 있는 이름입니다" )
    elif N == 2:
        print( f"이름: {str(ls)}" )
    elif N == 3:
        d_name = input("삭제할 이름: ")
        if ls.count(d_name) != 0:
            ls.remove(d_name)
            print( "삭제 완료" )
        else:
            print( "존재하지 않는 이름" )
    elif N == 4:
        pass
    elif N == 5:
        print( "종료" )
        break
    else:
        print( "올바른 번호 입력" )
        continue