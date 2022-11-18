'''
set
- 중복된 데이터 허용하지 않음
- 순서를 유지하지 않음
사용 방법
- set(데이터)
- {값, 값, ...}
'''
'''
s = {"안녕하세요"}
print( s )
print( type(s) )

s = set([1,1,1,2,3,4,4])
print( s )
#print( s[0] )   # 인덱스로 접근 불가
li = list(s)     # 리스트로 형변환해서 접근해야 함
print( li )
print( li[0] )


print( "-" )
'''

s = {1,2,3}
print( "변경 전:", s )
s.add(555)
print( "add", s )
s.update([4,5,6])
print( "update:", s )
s.remove(555)
print( "remove:", s )
print( "issuperset:", s.issuperset({1,2}) )
