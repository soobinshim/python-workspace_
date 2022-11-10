flt = 123.123
print( flt + 100 )

st1, st2 = "파", "이썬"
print( st1 + st2 )
#print( st1 + flt ) error

print ( "-" )

num = 100
print( type(num) )  # int(정수 형태)
num = "100"
print( type(num) )  # str(문자 형태)
num = 123.123
print( type(num) )  # float(실수 형태)

num = "100"
print( int(num) + 100 ) # int() 정수로 형변환


print( "-" * 100 )


#Q1.
print( "#Q1. 연산 ")
su = 100
num = '100'
flt = "1.111"
print( su + int(num) )
print( su + float(flt) )
print( str(su) + num )


print( "-" * 100 )


flt = "1.111"
print( type(flt), flt )
#print( int(flt) ) error. 문자 형태이기 때문에 실수로 먼저 변환 후 정수 형태로 변환해야 함
print( int(float(flt)) )

su = 100
num = '100'
print( su, float(su) )
print( num, float(num) )