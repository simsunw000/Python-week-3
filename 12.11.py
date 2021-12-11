lst = []

lst = [1,2,3,4]
lst2 = [5,6,7,8]

print('현재 리스트 1', lst)
print('현재 리스트 2', lst2)

#리스트 순서에 맞게 값 뽑기(index 활용)

index = int(input('인덱스를 입력해주세요.(인덱스 값의 범위 0 ~ 리스트 길이 -1) >>'))
print(f'인덱스 번호: {index}')
print(f'해당 번호에 해당하는 리스트1의 요소 {lst[index]}')
print(f'해당 번호에 해당하는 리스트1의 요소 {lst2[index]}')

# 인덱스의 범위
# 일반적으로는 0부터 길이 -1 까지 범위를 가진다
#Python에서는 음수의 번호가 존재한다. -1부터 길이 잼
#ex) 리스트 길이 4일 경우 -1 ~-4까지
#인덱스의 범위를 잘못 입력할 경우 오류 발생

# 슬라이싱 : 특정 범위를 잘라서 표현하는 파이썬 문법
# 사용방법 : 문자열, 자료구조 [인덱스값 : 개수]
s = 'hello, my name is brown'

print(s[0:5])

print('리스트 슬라이싱')
print('현재 리스트 1', lst)
index = int(input('인덱스값을 입력해주세요.(인덱스 값의 범위 0 ~ 리스트 길이 -1) >>'))
length = int(input('작업할 양을 입력해주세요.'))
print(f'슬라이싱 결과 = {lst[index : length]}')

#반복문에서 리스트 값 뽑기

for a in lst :
    print(a, end = ' ')



