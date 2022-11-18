st = {"학번":1234, "이름":"홍길동"}
print(st)
print(st.items()) #key와 값을 쌍으로 같이 가져옴
#for i in st.keys()
for k,v in st.items():
    print(f'{k} : {v}')

print(st.setdefault("학번",5555)) #key가 존재하면 데이터 추가 안함
print(st.setdefault("학번1",5555))
print(st)
print()

ls = [10,{"키":"키에의한 값"},30] #리스트 안에 딕셔너리를 넣을 수 있다
print( ls[0] )
dic = ls[1]
print( ls[1], ls[1]["키"], dic["키"] )
print( ls[2] )

dic = {"li":[10,20,30],"k":"value"} #딕셔너리 안에 리스트를 넣을 수도 있음
print( dic["li"][2])
print( dic["k"])

info = {}
info02 = {}

info02['가수'] = "개가수"
info02['인원수'] = 3
info02['노래명'] = "신나리"
info[info02['가수']] = info02.copy()

print( info02 )
print( info )
print()

for k, v in info.items():
    print(k)
    print(v)
    for kk, vv in v.items():
        print(kk,":",vv)

info02['안녕'] = '하세요'
print('-'*10)
print( info )
print( info02 )   #얕은 복사이기 때문에 같이 변경된다 (copy를 사용하면 서로 다르게 저장가능)

info = {} #초기화 방법1
info.clear() #초기화 방법2