'''
st = 'Never ever give up'
print( st )
print( st.split() ) # 공백을 기준으로 잘라서 리스트로 만들어 줌
print( st.split("e") )


print( "-" * 100 )


#Q1.
print( "#Q1." )
st = "안녕하세요 오늘 2300/5/14 날씨는 error 춥다"
st_ls = st.split()
#print( st_ls )
st_ls2 = st_ls[2].split("/")
#print( st_ls2 )
del(st_ls[4])
del(st_ls[2])
#print( st_ls )
st_ls.insert(2, st_ls2[0]+"년"+st_ls2[1]+"월"+st_ls2[2]+"일")
print( st_ls )

st = ""
for i in st_ls:
    st += i + " "
print( st )

################# 사실 이거 하나면 됨 print( " ".join(st_ls) ) ########################

print( "-" * 100)


st = "안녕하세요 반갑습니다"
print( st )
print( st.splitlines() )    # 엔터값을 기준으로 잘라서 리스트로 만들어 줌

st = """
안녕하 세 요
안녕하 세 요
아니"""
print( st.splitlines() )
print( st.split("\n") )


print( "-" )


st = "123"
test = "%"
print( test.join(st) )  # 앞에 있는 값을 뒤쪽 값의 사이사이에 넣어 줌
print( "$".join(st) )

print( st.join("안녕하세요") )

li = ["", "123", "456"]
print( "그래".join(li) )


print( "-" )


st = "python"
print( st )
print( st.center(10) )  # 10 칸 확보 후 가운데 정렬
print( st.center(10, "-") )

print( st.ljust(10) )  # 10 칸 확보 후 왼쪽 정렬
print( st.ljust(10, "-") )

print( st.rjust(10) )  # 10 칸 확보 후 오른쪽 정렬
print( st.rjust(10, "-") )

print( st.zfill(10) )


print( "-" * 100 )


#Q2.
print( "#Q2." )
accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"

replaceAB = accountBook.split(',')  # , 기준으로 리스트로 저장
print(replaceAB)

k = 0
for i in replaceAB:
    replaceAB[k] = i.lstrip()   # 각 문자열의 왼쪽 공백 삭제 후 저장(_coffee,_food,_dress)
    k += 1

print( 'item'.ljust(10), end="" )
print( 'date'.ljust(10), end="" )
print( '$(price)'.ljust(10) )
print( "-" * 30 )

kk = '$ '
for i in range(len(replaceAB)):
    z = replaceAB[i].split()    # 공백을 기준으로 리스트로 저장
    #[shoes, 03/02, 59000]
    #[coffee, ... ]
    #[food, ...]
    #[dress, ...]
    for k in range(len(z)):
        if k == 0 :
            print( z[k].ljust(10), end="" ) # 10 칸 확보 후 왼쪽 출력
        elif k == 1 :
            print( z[k].ljust(10), end="" ) # 10 칸 확보 후 왼쪽 출력
        elif k == 2 : 
            print( "{:,}".format(int(z[k])).join(kk).ljust(10) )


print( "-" )


accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"

x = accountBook.split(",")
print( "item\tdate\t$(price)" )
print( "-" * 24 )
for i in x:
    y = i.split()
    print( f"{y[0]}\t{y[1]}\t${int(y[2]):,}" )


print( "-" * 100 )


st = "python te12st 1234"
print( st.isdigit() )   # 숫자로만 구성
print( st[9:11].isdigit() )

print( st.isalpha() )   # 알파벳으로만 구성
print( st[:6].isalpha() )

print( st.isalnum() )   # 알파벳+숫자로만 구성
print( st[7:13].isalnum() )

print( st.islower() )   # 알파벳 소문자로만 구성
print( st.isupper() )   # 알파벳 대문자로만 구성
print( st.isspace() )   # 공백으로만 구성


print( "-" * 100 )


#Q3.
print( "#Q3." )
info = """
jo 9abc08-3022023
cho 900402-1011232
test 1234567-1234567 
lee 980908-3a2b0c3
kim 900514-2022023
"""

print( info )

k = 0
for i in range( info.count("-") ): 
    k = info.find("-", k+1)

    if info[k+1:k+8].isdigit() and not info[k-7:k].isdigit() and info[k-6:k].isdigit():
        info = info.replace(info[k+1:k+8], "*******")
print( info )


print( "-" * 100 )
'''

#Q4.
print( "#Q4." )

st = ""
print( "png : ", st.count(".png") )
print( "jpg : ", st.count(".jpg") )
print( "gif : ", st.count(".gif") )

j = 1
for i in st.split('src'):
    for k in i.split():
        if k.find(".jpg") != -1 or k.find(".png") != -1 or k.find(".gif") != -1:
            k = k.split("/")
            print( j,".",k[-1] )    # 마지막 특수문자 포함 출력

            # 마지막 특수문자 제거
            
            index = k[-1].find(".jpg") + k[-1].find(".png") + k[-1].find(".gif")
            #print(f"index:{index}, {k[-1].find('.jpg')},{k[-1].find('.png')}, {k[-1].find('.gif')} ")
            print( j,".",k[-1][:index+6] )
            j += 1
            print( "-" * 30 )
print( "총 개수 : ", st.count(".png") + st.count(".jpg") + st.count(".gif") )














