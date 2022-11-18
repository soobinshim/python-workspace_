'''
def func01(*par):
    print( type(par) )
    for i in par:
        print(i)
func01(10,20,30,40)

def big(a,b):
    if a>b:
        return a
    else:
        return b
result = big(10,20)
print(result)
'''

#람다 함수의 사용법
'''
bi = lambda a,b : a if(a>b) else b #a,b를 매개변수로 받을 때, if 문이 참이라면 a를 반환  else 라면 b를 반환해준다는 의미.
result = bi(200,1000)
print(result)

bi = lambda a : a + 1000
print(bi(100))
'''

#문제)
'''
print("-"*10)
li = ['100','200','300']
print("변경 전 : ",li)
for i in range( len(li) ):
    li[i] = str( int(li[i])+10 )
print("변경 후 : ",li)

print("-"*10)
li = ['100','200','300']
print("변경 전 : ",li)

li = list( map(int, li) )
print("변경 후 : ",li)

for i in range( len(li) ):
    li[i] = str( li[i]+10 )
print("변경 후 : ",li)


li = ['100','200','300']
def test1( a ):
    return str(int(a)+10)

li = list(map(test1, li))
print("함수 : ",li)

print("---------")

'''

'''
li = ['100','200','300']
lb = lambda x: str(int(x)+10)
li = list(map(lb,li))
#li = list(map(lambda x: str(int(x)+10),li))
print('lambda:', li)
'''


'''
day={'날짜':[ '2018.01.01', '2019.02.02', '2020.03.03' ]} #딕셔너리, 키와밸류 중 밸류는 리스트로 저장된형태.
for key,values in day.items():
    #print(values)
    for i in values:
        #print(i)
        v=i.split('.')
        print(v)
        print(f'{v[0]}년{v[1]}월{v[2]}일')
'''


day={'날짜':[ '2018.01.01', '2019.02.02', '2020.03.03' ]} #딕셔너리, 키와밸류 중 밸류는 리스트로 저장된형태.
lb = lambda x : x.split('.')
print(day['날짜'],type(day['날짜']))
ls = list(map(lb, day['날짜']))# map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜주어야 합니다.
#ls = list(map(lambda x : x.split('.'), day['날짜']))
for v in ls:
    print(v)
    print(f'{v[0]}년{v[1]}월{v[2]}일')