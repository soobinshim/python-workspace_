'''
딕셔너리
- Key와 Value 하나의 쌍으로 이루어져 있다
- 탐색 속도가 빠르며 사용하기 편리하다
 {key:value}
'''

st = {"stNum":1234, "이름":"홍길동"}
print( st )
print( type(st) )

mobile = {"품명":"갤럭시","가격":1000}
print( mobile )
print( mobile["품명"] )

impo = {}
impo['파이썬'] = "www.python.org"
impo['네이버'] = "www.naver.com"
print( impo["파이썬"] )
print( impo["네이버"] )


impo = {}
name = input("등록할 키 입력: ")
value = input("등록할 값 입력: ")
impo[name] = value
print( impo )
print( impo[name] )


print( "-" )


num = {1:"일", 2:"이", 3:"삼"}
print( num.keys() )
print( num.values() )

print( type(num.keys) )

li = list(num.keys())
print(li, li[0])

for i in num.keys():
    print( i,":",num[i] )
print()

num = {1:"일", 2:"이", 3:"삼"}
print( num[1])
print( num.get(1))

#print( num[111])
print( num.get(111))

key = int(input("key 입력 : "))
result = num.get(key)
if result == None:
    print("찾는 내용이 없습니다.")
else:
    print( key,":",result)