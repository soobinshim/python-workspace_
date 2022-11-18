'''
사용모드
-w : 파일에 내용출력
-r : 파일에 내용가져오기
-wb : 텍스트가 아닌 이미지, 동영상 등 '바이너리'로 처리되는값 출력
-rb : 읽어오기
'''
'''
file = open('C:/0. k-디지털/python-workspace/test.txt','w')# w :이미 내용이 존재할경우 그내용파괴하고 새로 적용
st = input('출력할 내용 입력:')
file.write(st)
file.close()
'''

'''
file = open('C:/0. k-디지털/python-workspace/test.txt','a')# a :이미 내용이 존재할경우 그내용에 더해줌
st = input('출력할 내용 입력:')
file.write(st)
file.close()
'''

'''
file = open('C:/0. k-디지털/python-workspace/test.txt','r')# r :파일에서 내용가져옴
st = file.read()
file.close()
print(st)
'''


'''
file = open('C:/0. k-디지털/python-workspace/Q01.txt','w')
x = input('이름입력:')
y = input('나이입력:')
z = input('주소입력:')
# str = ''
str = x + '\n' + y + '\n' + z
file.write(str)
#file.close()
'''



'''
#복붙코드
w_file = open('C:/0. k-디지털/python-workspace/test1.txt','w')#오픈이라는 기능을 통해 파이썬과 파일위치를 스트림(연결)을 해준다
r_file = open('C:/0. k-디지털/python-workspace/test.txt','r')
#print(r_file.read()) 여기서 이코드를 실행하게 되면 아래가 원하는대로 처리되지않는다.
w_file.write(r_file.read()) # ****중요**** write 를 통해 파일에 내용 저장을 하고 싶다면 반드시 close()를 세트로 써주자.
# w_file.flush()
w_file.close()#그래야 내용이 증발하지않고 다음에 열어도 저장이 되어있다.
r_file.close()
'''

'''
file = open('C:/0. k-디지털/python-workspace/abcd.txt','w',encoding='utf-8')
st = input("입력: ")
file.write(st)
file.close()
'''


'''
r_file = open('C:/0. k-디지털/python-workspace/abcd.txt','r', encoding='utf-8')
print(r_file.read())
r_file.close()
'''




'''
r_file = open('D:/11_07_k-디지털 김남규/test.txt','r')
'''
#방식1
'''
st= r_file.read()
print(st)
print(type(st))

s1 = r_file.readline()
s2 = r_file.readline()#한줄씩 가져오기
s3 = r_file.readline()
s4 = r_file.readline()
print(s1)
print(s2)
if s4 =='':
    print('더이상 데이터 없음.')
'''

#방식2
'''
while True:
    s=r_file.readline()
    if s =='':
        print('데이터없음')
        r_file.close()
        break
    print(s, type(s))
'''
#방식3
'''
s= r_file.readlines()
print('----lines-----')
print(s, type(s))
r_file.close()

for i in range(len(s)):
    print(f'{i}.{s[i]}')
for i,v in enumerate(s):#자동으로 번호매겨주는 함수
    print(i,v)
'''



#문제)
'''
w_file = open('D:/11_07_k-디지털 김남규/quest01.txt','w')
st01 = input('내용 입력:')
st02 = input('내용 입력:')
st03 = input('내용 입력:')
w_file.write(st01+'\n'+st02+'\n'+st03)
w_file.close()
'''

'''
r_file = open('D:/11_07_k-디지털 김남규/quest01.txt','r')
s = r_file.readlines()#줄별로 읽어보고, 파일의 각 라인을 리스트 객체로 반환
print(s)
#r_file.close() 질문
for i,v in enumerate(s):#알아서 번호 매겨서 출력해주기
    print(i,":",v)

num = int(input('수정할 번호 입력:'))
value = input('수정값입력 : ')
if len(s)-1 == num:
    s[num] = value
else :
    s[num] = value +'\n'
r_file.close()

file = open('D:/11_07_k-디지털 김남규/quest01.txt','w')
for i in s:
    file.write(i)
file.close()
'''
#파일 존재여부 및 존재할때 파일 읽어오는 코드
'''
path = 'D:/11_07_k-디지털 김남규/'
import os
fileName = input('파일명 입력:')
path += fileName+'.txt'
print(os.path.exists(path))#파일이름이 저기 path쪽 폴더안에 존재하는 파일이면 트루반환
if os.path.exists(path):
    file = open(path,'r')
    print('----파일읽기---')
    print(file.read())
    file.close()
'''