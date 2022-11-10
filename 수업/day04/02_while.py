'''
while 조건식:
    종속 문장
'''

i = 0
while i < 5:
    print( i, "종속 문장" )
    i += 1
print( "다음 문장" )


for i in range(5):
    print( i, "종속 문장" )
print( "다음 문장" )


print( "-" )


i = 1
even = 0
odd = 0
while i <= 10:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    i += 1
print( f"1~10까지의 짝 합: {even}" )
print( f"1~10까지의 홀 합: {odd}" )


even = 0
odd = 0
for i in range(1, 11):
    if i % 2 == 0:
        even += i     
    else:
        odd += i
print( f"1~10까지의 짝 합: {even}" )
print( f"1~10까지의 홀 합: {odd}" )
        