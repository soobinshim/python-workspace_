'''
tuple
- 중복된 데이터 허용하지 않음
- 데이터의 변경이 불가능
- index 접근 가능하다
- (소괄호)로 표현한다
'''

tp = (10,20,30)
print( tp )
print( type(tp) )
print( tp[0] )
print( len(tp) )

#tp[0] = 1234   # 특정 값을 변경할 순 없다
tp = (10)
print( tp,":",type(tp) )

tp = (10,)
print( tp,":",type(tp) )

tp = 10,
print( tp,":",type(tp) )


'''
패킹: 압축(여러 개의 값을 하나의 공간에 저장)
언패킹: 하나의 덩어리를 여러 개의 공간에 저장
'''

tp = 1, 2, "패킹", 3, 4, 5
print( "패킹", tp )
a,b,c,d,e,f = tp
print( a,b,c,d,e,f )

a,b,*c = tp
print(a,b,c)

tp = 100,200,300,100
print( tp.index(200) )
print( tp.count(100) )