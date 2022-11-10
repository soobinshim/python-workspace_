
for i in range(0,3,1):
    print( "상위 for문 실행" )
    for k in range(0,5,1):
        print( f"이중 for문 (i: {i}, k: {k})" )
    print( "종료 상위 for문" )


print( "-" * 100 )


#Q1.
print( "#Q1. 구구단" )
for i in range(2, 10, 1):
    print( f"{i}단" )
    for k in range(1, 10, 1):
        print( f"{i} * {k} = {i * k}" )
    print()


print( "-" * 100 )


#Q2.
print( "#Q2." )
for i in range(0, 5, 1):
    print( f"상위 포문 {i}일 때 하위 포문:", end=" " )
    for k in range(0, 5, 1):
        print( f"{i * k}", end=" " )
    print()


print( "-" * 100 )


#Q3.
for i in range(0, 5, 1):
    for k in range(1, 6, 1):
        print( (i * 5) + k, end="\t" )
    print()



            