'''
리스트
- 여러 개의 값을 저장할 경우 사용
- 순서를 가지고 있다
- index는 0부터 시작한다
- [] (대괄호)로 표현한다
'''
'''
ls = [500, 200, 300, 400]
print( ls )
print( ls[0], ls[3] )


print( "-" )


ls = [0,0,0,0]
ls[0] = int(input("0.수 입력: "))
ls[1] = int(input("1.수 입력: "))
ls[2] = int(input("2.수 입력: "))
ls[3] = int(input("3.수 입력: "))

sum_ = ls[0] + ls[1] + ls[2] + ls[3]
print( "합: ", sum_)

print( "-" )

ls = [0,0,0,0]
print( "len: ", len(ls) )
sum_ = 0
for i in range(len(ls)):
    ls[i] = int(input(f"{i}.수 입력: "))
    sum_ += ls[i]
print( "합: ", sum_)


print( "-" )
  

ls = [0,0,0,0]
ls[0] = int(input("0.수 입력: "))
ls[1] = int(input("1.수 입력: "))
ls[2] = int(input("2.수 입력: "))
ls[3] = int(input("3.수 입력: "))

for i in range(len(ls)):
    print(f"ls[{i}]: {ls[i]}")
print( "-" )
for i in "abcd":
    print( i )
print( "-" )
for i in ls:    # [10,20,30,40]
    print( i )


print( "-" )


ls = [10,20,30,40,50]
print( ls )
print( "-" )
print( ls[0:3] )
print( ls[2:] )
print( ls[:2] )


print( "-" )


ls = [10,20,30,40]
#arr = ls    # 얕은 복사 (ls와 같은 공간을 씀)
#arr = ls[:] # 깊은 복사 (ls 데이터 자체를 넘겨받아서 다른 공간을 씀)
arr = ls.copy()
arr[0] = "안녕"
print( ls, ":", id(ls) )
print( arr, ":", id(arr) )


print( "-" )


ls = [10,20,30]
arr = [40,50,60]
print( ls )
print( arr )

arr02 = ls + arr
print( arr02 )

arr03 = ls * 3
print( arr03 )


print( "-" * 100 )


#Q1.
print( "#Q1." )
ls = [10,20,30]
arr = [40,50,60]

str = [0,0,0]
string = [0,0,0]
for i in range(len(ls)):
    str[i] = ls[i] + arr[i]
for i in range(len(ls)):
    string[i] = ls[i] * 3
print( str )
print( string )


print( "-" * 100 )


#Q2.
print( "#Q2." )
print( "1)" )
ls = [10,5,20,7,9,31,12,11,19,32]

evenSum = [0,0,0,0,0]
oddSum = [0,0,0,0,0]
result = [0,0,0,0,0]
index = 0
for i in range(len(ls)):
    if i % 2 == 0:
        evenSum[index] = ls[i]
    else:
        oddSum[index] = ls[i]

        index += 1
print( f"짝수 번째 값: {evenSum}" )
print( f"홀수 번째 값: {oddSum}" )

for i in range(len(evenSum)):
    result[i] = evenSum[i] - oddSum[i]
print( f"결과: {result}" )

print( "2)" )
esum = osum = 0
for i in range(len(evenSum)):
    esum += evenSum[i]
    osum += oddSum[i]
print( f"차: {osum - esum}" )

print( "3)" )
invertLS = [0,0,0,0,0,0,0,0,0,0]
size = len(ls)
for i in ls:
    size -= 1
    invertLS[size] = i
print( ls )
print( invertLS )
'''

print( "-" * 100 )


#Q3.
print( "#Q3. 순위 구하기" )
score = [82, 85, 76, 79, 96]
rank = [1,1,1,1,1]
for i in range( len(score) ):
    for k in range( len(score) ):
        if score[i] < score[k]:
            rank[i] += 1
    print( f"점수: {score[i]}\t등수: {rank[i]}" )

i = 0
print( "점수\t등수" )
while i < 5:
    print( f"{score[i]}\t{rank[i]}" )
    i += 1



