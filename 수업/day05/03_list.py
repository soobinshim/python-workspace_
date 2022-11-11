# 다차원 리스트
# ls = [ [값],[값],[값] ]
ls = [ [1,[2,100,200],3,4],[5,6,7,8],[9,10,11,12] ]
print( ls[0] )
print( ls[0][1] )
print( ls[0][1][2] )

ls = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]
print( ls[0][0] )
print( ls[0][1] )
print( ls[0][2] )
print( ls[0][3] )

print( ls[1][0] )
print( ls[1][1] )
print( ls[1][2] )
print( ls[1][3] )


print( "-" * 100 )


# Q1.
print( "#Q1." )
ls = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]
for i in range( 3 ):        # len(ls)
    for k in range( 4 ):    # len(ls[i])
        print( ls[i][k], end="\t" )
    print()


ls = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]
for i in ls:
    #print( i )
    for k in i:
        print( k, end= "\t" )
    print()


print( "-" * 100 )


ls = [ [1,2,3,4],[5,6,7,8] ]
#arr = ls[0]        # 얕은 복사
#arr = ls[0][:]      # 깊은 복사
arr = ls[0].copy()  # 깊은 복사
arr[1] = 1000

print( ls )
print( arr )


print( "-" * 100 )


#Q2.
print( "#Q2." )
ls_1 = []
ls_2 = []
value = 1

for i in range(3):
    for k in range(4):
        ls_1.append(value)
        value += 1  
    ls_2.append(ls_1)
    ls_1 = []
print( f"ls_2: {ls_2}" )

for i in range(len(ls_2)):
    for k in range(len(ls_2[i])):
        print( ls_2[i][k], end="\t" )
    print()

print( "-" )

while value < 13:
    ls_1.append(value)
    if value % 4 == 0:
        ls_2.append(ls_1)
        ls_1 = []
    value += 1
print( ls_2 )


print( "-" * 100 )


ls = [10,20,30]
s = ls[0] * 100
print( s )

ls = ['10','20','30']
s = list(map(int, ls))    # 리스트 안의 모든 값들은 int 형태로 변환해 준다
print( s )

ls = ['10','20','30']
s = []
for i in ls:
    s.append(int(i))
print( s )