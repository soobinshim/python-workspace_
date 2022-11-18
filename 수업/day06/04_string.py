'''
st = "Have a nice day"
print( st )

print( st[0] )
print( st[1] )
print( st[-1] )

print( len(st) )

for i in range(len(st)):
    print( st[i], end="" )
print()

for i in st:
    print( i, end="" )


print( "-" )


st = "Have a nice day"
print( st[3:6] )

st = "Python test. 그리고 programming 할 만하다 ^^"
print( st )
print( st.upper() ) # 대문자로 변경
print( st.lower() ) # 소문자로 변경
print( st.swapcase() )  # 대/소문자 상호 변경
print( st.title() ) # 단어의 첫 글자 대문자로 변경


print( "-" * 100 )


#Q1.
print( "#Q1. 단어 첫 글자들 대문자로" )
st = "NevEr -eVer 110gIve up"
print( "변경 전:", st)
#st = st.title()
print( "변경 후:", st.title() )


print( "-" * 100 )


st = "Have a nice day"
print( st )
print( st.count('a') )  # 해당 문자 개수
print( st.count('day') )
print( st.count('dak') )

print( st.startswith('Ha') )    # 시작 문자
print( st.startswith('ha') )

print( st.endswith('day') )    # 끝 문자
print( st.endswith('da') )


print( "-" * 100 )


#Q2.
print( "#Q2. 아래 문자열의 총 개수, 'a'개수, 's' 개수 출력" )
st = "It is a fun Python class"

print( f"총 개수: {len(st)}" )
print( f"'a' 개수: {st.count('a')}" )
print( f"'s' 개수: {st.count('s')}" )


print( "-" * 100 )


st = "Have a nice day"
print( st )
print( st.find('day') )
print( st.index('day') )
print( st.find('dddd') )
#print( st.index('dddd') )

st = "Have a nice day"
print( st.find('a') )   # 제일 앞쪽의 a만 찾아 줌
print( st.find('a', 2) )    # 2 번째부터 a 찾아
print( st.find('a', 6) )    # 6 번째부터 a 찾아


print( "-" )


st = "Have a nice day"

num = st.find('a')
print( st.find('a') )
print( st.find( 'a', num+1) )

num = st.find('a', num+1)
print( st.find('a', num+1) )


print( "-" * 100 )


#Q3.
print( "#Q3." )
st = 'Have a nice day Have a nice day Have a nice day'
ls = []
cnt = 0

for i in st:
    cnt = st.find('a', cnt)
    if cnt != -1:
        ls.append(cnt)
        cnt += 1

print( "a 개수:", st.count('a') )
print( "a 위치:", ls )


print( "-" * 100 )


#Q4.
print( "#Q4." )
li = ['AbCe test123', '.acd efg', 'a123 TEST 123', '123 TEst']

for i in li:
    ls = i.lower()

    if ls.startswith('ab') or ls.endswith('test'):
        print( i )


print( "-" * 100 )


st = '    파이썬 '
print( f"*{st}*")
print( f"*{st.strip()}*")   # 공백 제거

name = input("이름 입력: ")
print( f"이름: {name}" )
if name.strip() == '홍길동':
    print( "인증 통과" )
else:
    print( "인증 실패" )


print( "-" )


st = "+++파이썬+++"
print( st )
print( st.strip("+") )
print( st.rstrip("+") )
print( st.lstrip("+") )


print( "-" )
'''

st = "2015/04/02"
print( st )
print( st.replace("/", ".") )
print( st.replace(st[0:4], "2022") )


print( "-" * 100 )


#Q5.
print( "#Q5." )
st = """
김개똥-2017년 03월 24일
홍길동구리-2015년 04월 02일
선우선녀-2018년 05월 14일
"""
st = st.replace("-", ":")
cnt = 0
for i in range(3):
    cnt = st.find(':', cnt+1)
    st = st.replace(st[cnt+1:cnt+5], "1999")
    #print( ls ) #4, 25, 45
print( st )

